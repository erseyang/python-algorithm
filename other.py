

def mul(n):
    def wrapper(m):
        return n * m
    return wrapper

def strappend(num):
    strt='first'
    for i in range(num):
        strt+=str(i)
    print(strt)
    return strt

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds.")
        return res
    return wrapper

@time_it
def my_function():
    print("Executing my_function...")
    time.sleep(2)

if __name__ == '__main__':
    # print(mul(2)(3))
    # strappend(5)
    my_function()