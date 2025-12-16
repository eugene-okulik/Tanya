def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


fib_gen = fib(70)

for num in fib_gen:
    if num == 5:
        print(num)
    elif 200 <= num < 300:
        print(num)
    elif 1000 <= num < 2000:
        print(num)
    elif 100000 <= num < 200000:
        print(num)
        break
