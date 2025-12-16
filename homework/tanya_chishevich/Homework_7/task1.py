num = 3
while True:
    input_number = int(input("Введите любую цифру: "))
    if input_number == num:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова...")
