a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"

result_first = a.index(':')
print(int(a[result_first + 1:]) + 10)

result_second = b.index(':')
print(int(b[result_second + 1:]) + 10)

result_third = c.index(':')
print(int(c[result_third + 1:]) + 10)
