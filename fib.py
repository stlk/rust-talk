import ctypes

library_name = "libfastblank/target/release/libfastblank.dylib"
stringtools = ctypes.CDLL(library_name)

def fib(n):
    """Calculate the n-th Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def slow():
    fib(37)

def fast():
    stringtools.fib(37)

if __name__ == '__main__':
    import timeit
    print("slow")
    print(timeit.timeit("slow()", setup="from __main__ import slow", number=1))
    print("fast")
    print(timeit.timeit("fast()", setup="from __main__ import fast", number=1))
