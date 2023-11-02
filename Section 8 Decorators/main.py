from time import time


def my_decorator(func):
    def wrap_func(x, y):
        print("*********")
        func(x, y)
        print("///////////////////")

    return wrap_func


@my_decorator
def hello(greeting, name):
    print(f"{greeting} {name}")


hello("hi mr", "omar")


def my_performance(func):
    def wrapper_func(*args, **kawrgs):
        t1 = time()
        result = func(*args, **kawrgs)
        t2 = time()
        print(f"time elapsed is {t2-t1} s")
        return result

    return wrapper_func


@my_performance
def performance():
    for i in range(10256006):
        i * 5


performance()
