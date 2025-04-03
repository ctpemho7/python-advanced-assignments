import multiprocessing
import threading
import time
from codecs import encode
from datetime import datetime


def output_listener(output_queue):
    """ Процесс получает из input_queue строку, делает .lower() и отправляет в output_queue строку раз в 5 секунд """
    while True:
        if not output_queue.empty():
            result = output_queue.get()
            print(f"[{datetime.now().time()}] Main: received from Process B - '{result}'")
        time.sleep(0.1)


def process_a(input_queue, output_queue):
    """ Процесс получает из input_queue строку, делает .lower() и отправляет в output_queue строку раз в 5 секунд """
    while True:
        if not input_queue.empty():
            # получить
            message = input_queue.get()
            # обработать
            processed_message = message.lower()
            # положить 
            output_queue.put(processed_message)
            print(f"[{datetime.now().time()}] Process A forwarded to Process B: '{processed_message}' ")
        time.sleep(5)


def process_b(input_queue, output_queue):
    """ Процесс применяет к строке кодировку rot13 и отправляет в output_queue """
    while True:
        if not input_queue.empty():
            message = input_queue.get()
            rot13_message = encode(message, 'rot13')
            print(f"[{datetime.now().time()}] Process B: encodes ROT13: '{rot13_message}'")
            output_queue.put(rot13_message)
            print(f"[{datetime.now().time()}] Process B forwarded to Main")


def main():
    # очереди
    main_to_a = multiprocessing.Queue()
    a_to_b = multiprocessing.Queue()
    b_to_main = multiprocessing.Queue()

    proc_a = multiprocessing.Process(target=process_a, args=(main_to_a, a_to_b))
    proc_b = multiprocessing.Process(target=process_b, args=(a_to_b, b_to_main))
    
    proc_a.start()
    proc_b.start()

    # создаем поток-демон читает b_to_main
    listener_thread = threading.Thread(
        target=output_listener,
        args=(b_to_main, ),
        daemon=True  
    )
    listener_thread.start()

    try:
        while True:
            user_input = input(f"[{datetime.now().time()}] Input your message:\n")
            print(f"[{datetime.now().time()}] Main: sending '{user_input}' to Process A")
            main_to_a.put(user_input)
            
    except KeyboardInterrupt:
        print("\nInterrupted!")
    finally:
        # Ожидаем завершения процессов
        proc_a.join()
        proc_b.join()
        print("\nStopped")


if __name__ == "__main__":
    main()