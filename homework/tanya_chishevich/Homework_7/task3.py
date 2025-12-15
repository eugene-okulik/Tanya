a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"
d = "результат: 2"


def get_number(*args):
    for i in args:
        result = i.index(':')
        print(int(i[result + 1:]) + 10)


get_number(a, b, c, d)
