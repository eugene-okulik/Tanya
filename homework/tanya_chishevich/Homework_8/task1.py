from random import randint, choice

salary = int(input("Введите вашу зарплату: "))
is_bonus = choice([True, False])
bonus = randint(100, 300)


def get_salary_bonus(s, is_b, b):
    if is_b:
        s += b
        print(f"Ваша зарплата c бонусом {b}: ${s}")
    else:
        print(f"Ваша зарплата без бонуса: ${s}")


get_salary_bonus(salary, is_bonus, bonus)
