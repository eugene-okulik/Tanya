a = float(input("Введите первое значение (a): "))
b = float(input("Введите второе значение (b): "))

# 1. Получаем среднее арифметическое двух чисел.
arithmetic_average = round(((a + b) / 2), 2)
print(f"Среднее арифметическое: {arithmetic_average}")

# 2. Получаем среднее геометрическое двух чисел.
geometric_average = round(((a * b) ** 0.5), 2)
print(f"Среднее геометрическое: {geometric_average}")
