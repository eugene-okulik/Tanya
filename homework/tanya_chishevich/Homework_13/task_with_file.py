import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            line = line.strip()

            parts = line.split(' - ', 1)
            if len(parts) == 2:
                date_text, other_text = parts
            date_parts = date_text.split('. ', 1)
            if len(date_parts) == 2:
                num, date = date_parts
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
                record_number = int(num)
                if record_number == 1:
                    print('Дата на неделю позже:', date_obj + timedelta(days=7))
                elif record_number == 2:
                    print(date_obj.strftime('День недели: %A'))
                elif record_number == 3:
                    now = datetime.now() - date_obj
                    print('Количество дней назад была дата(date_obj):', now.days)
                else:
                    print(f"Нет такого номера №{record_number} в файле")
            except ValueError:
                print(f"Не удалось разобрать дату или номер в строке")


read_file()
