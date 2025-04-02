import time
import threading
import multiprocessing


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {end_time - start_time:.2f} secs")
        return result
    return wrapper


def fib(n: int):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@timeit
def run_sync(n: int, iterations=10):
    for _ in range(iterations):
        fib(n)


@timeit
def run_threads(n: int, iterations=10):
    threads = []
    for _ in range(iterations):
        t = threading.Thread(target=fib, args=(n,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


@timeit
def run_processes(n: int, iterations=10):
    processes = []
    for _ in range(iterations):
        p = multiprocessing.Process(target=fib, args=(n,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


if __name__ == "__main__":
    n = 40
    iterations = 10

    print(f"Вычисление {iterations} раз числа Фибонначи от {n}...")

    run_sync(n, iterations)
    run_threads(n, iterations)
    run_processes(n, iterations)