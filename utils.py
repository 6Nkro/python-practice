import time
# pip install memory-profiler
from memory_profiler import memory_usage

def benchmark(func):
    def wrapper(*args, **kwargs):
        start_mem = memory_usage()[0]
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        end_mem = memory_usage()[0]
        mem_diff = end_mem - start_mem

        print(f"{func.__name__} 함수 실행 시간: {elapsed_time:.4f} 초")
        print(f"{func.__name__} 함수 메모리 사용량: {mem_diff:.4f} MiB\n")

        return result
    return wrapper