first_leg = float(input("Введите длину первого катета (first_leg): "))
second_leg = float(input("Введите длину второго катета (second_leg): "))

# 1. Получаем гипотенузу прямоугольного треугольника.
hypotenuse = round((first_leg ** 2 + second_leg ** 2) ** 0.5, 2)
print(f"Гипотенуза равна: {hypotenuse}")


# 2. Получаем площадь прямоугольного треугольника.
square = round(((first_leg * second_leg) / 2), 2)
print(f"Площадь равна: {square}")
