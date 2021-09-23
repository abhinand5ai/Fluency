import timeit
from functools import cache, lru_cache


def fib(n: int):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=3)
def fib_cached(n: int):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    SETUP_CODE = '''
from __main__ import fib,fib_cached
'''
    fibTime = timeit.repeat(setup=SETUP_CODE, stmt="fib(33)", repeat=1, number=10)
    print("fib without cache took {} sec".format(fibTime))
    fibTime = timeit.repeat(setup=SETUP_CODE, stmt="fib_cached(33)", repeat=1, number=10)
    print("fib with cache took {} sec".format(fibTime))
