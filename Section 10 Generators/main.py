from time import time


def generator_function(n):
    for i in range(n):
        yield i * 2


g = generator_function(5)
next(g)
print(next(g))

# generators.

# generators are much more performant than lists. (i.e range > list in performance.)

# So generators are really, really useful when calculating large sets of data.


def performance(fnc):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fnc(*args, **kwargs)
        t2 = time()
        print(f"it took almost {t2-t1} s")
        return result

    return wrapper


@performance
def longtime():
    print("without using lists")
    for i in range(100000000):
        i * 5


longtime()


@performance
def longtime2():
    print("using lists")
    for i in list(range(100000000)):
        i * 5


longtime2()
