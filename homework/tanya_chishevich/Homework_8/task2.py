import sys

sys.set_int_max_str_digits(100001)


def fib():
    a, b = 0, 1
    count = 1
    while True:
        if count == 5:
            yield a
        elif count == 200:
            yield a
        elif count == 1000:
            yield a
        elif count == 100000:
            yield a
        a, b = b, a + b
        count += 1


fib_gen = fib()

for num in fib_gen:
    print(num)
