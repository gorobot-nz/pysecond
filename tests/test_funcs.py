b = 15


def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fib(num-1) + fib(num-2)


def func(num):
    return (num ** 2) * b


def func_2(num):
    return num * func(num)


def another_func_1(num):
    return num ** 2


def another_func_2(num):
    return num * 3


def another_func(num):
    ans = 1
    while ans < 10:
        ans *= another_func_1(num) * another_func_2(num)
    return ans
