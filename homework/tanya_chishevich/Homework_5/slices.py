a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"

result_first = a.index('42')
print(int(a[result_first:]) + 10)

result_second = b.index('514')
print(int(b[result_second:]) + 10)

result_third = c.index('9')
print(int(c[result_third:]) + 10)
