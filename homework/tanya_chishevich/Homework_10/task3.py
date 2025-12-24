NUM1 = 'Введите первое число: '
NUM2 = 'Введите второе число: '

def decorator(func):
    def wrapper(a, b, operation):
        if a == b:
            return func(a, b, '+')
        elif a > b:
            return func(a, b, '-')
        elif b > a > 0:
            return func(a, b, '/')
        elif a < 0 or b < 0:
            return func(a, b, '*')

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


calc1 = calc(int(input(NUM1)), int(input(NUM2)), '+')
print(calc1)
calc2 = calc(int(input(NUM1)), int(input(NUM2)), '-')
print(calc2)
calc3 = calc(int(input(NUM1)), int(input(NUM2)), '/')
print(calc3)
calc4 = calc(int(input(NUM1)), int(input(NUM2)), '*')
print(calc4)
