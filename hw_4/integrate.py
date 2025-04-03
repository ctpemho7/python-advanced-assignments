import concurrent
import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_ex(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate_range(f, a, b, n_iter):
    """ Интегрирование функции f на отрезке от a до b с точностью n_iter """
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


# def integrate_range(f, start, end, step):
#     """ Функция для вычисления итеграла на отрезке start до end с шагом step """
#     partial_acc = 0.0
#     for i in range(start, end):
#         partial_acc += f(start + i * step) * step
#     return partial_acc


def integrate(pool_class, f, a, b, n_jobs=1, n_iter=10000000):
    # Определяем границы для каждого пула, по сути на каждый пул будет |a-b| / n_jobs 
    chunk_size = abs(a-b) / n_jobs
    starts = []
    ends = []
    for i in range(n_jobs):
        starts.append(a + i * chunk_size)
        ends.append((i + 1) * chunk_size if i < n_jobs - 1 else b)
    iter_per_job  = n_iter // n_jobs

    with pool_class(max_workers=n_jobs) as executor:
        futures = [ executor.submit(integrate_range, f, starts[i], ends[i], iter_per_job) for i in range(n_jobs) ]
        acc = 0
        for future in concurrent.futures.as_completed(futures):
            acc += future.result()
    return acc


def main():
    func = math.cos
    a, b = 0, math.pi / 2
    n_iter = 10000000
    number_of_cpus = os.cpu_count()

    start_time = time.time()
    result = integrate_ex(func, a, b)
    time_original = time.time() - start_time 
    print(f"Result of original function: {result:.4f} of time {time_original:.4f}s")

    for n_jobs in range(1, 2*number_of_cpus+1):
        start_time = time.time()
        result_thread = integrate(ThreadPoolExecutor, func, a, b, n_jobs, n_iter)
        thread_time  = time.time() - start_time 

        start_time = time.time()
        result_process = integrate(ProcessPoolExecutor, func, a, b, n_jobs, n_iter)
        process_time  = time.time() - start_time 

        print(f"n_jobs={n_jobs:2d} | ThreadPool: {thread_time:.4f}s, result: {result_thread:.4f} | ProcessPool: {process_time:.4f}s, result: {result_process:.4f}")

if __name__ == "__main__":
    main()