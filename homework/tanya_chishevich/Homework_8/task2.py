import sys

sys.set_int_max_str_digits(100001)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fib()
positions = [5, 200, 1000, 100000]
results = {}

for pos in positions:
    num = 0
    for i in range(pos):
        num = next(fib_gen)
    results[pos] = num

print(f"Пятое: {results[5]}")
print(f"Двухсотое: {results[200]}")
print(f"Тысячное: {results[1000]}")
print(f"Стотысячное: {results[100000]}")
