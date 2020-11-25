import functools


def pamiec(func):
    memory = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        n = args[0]
        fib_n = memory.get(n, -1)
        if fib_n == -1:
            memory[n] = func(n)
        return memory[n]
        # tu powinien być kod tworzący słownik (element - wartość), który jest sprawdzany
        # do obliczeń wyrazów ciągu - które by były wyliczane rekurencyjnie i wpisywane
        # do słownika tylko gdy wcześniej nie były obliczone
        # normalnie bez buforowania by było return func(*args, **kwargs)

    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


for i in range(100):
    print(fibonacci(i))

