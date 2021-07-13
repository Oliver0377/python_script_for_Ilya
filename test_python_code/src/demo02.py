import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def wast_some_time(time_number):
    for s in range(time_number):
        sum([i ** 2 for i in range(10000)])


if __name__ == "__main__":
    wast_some_time(1)
