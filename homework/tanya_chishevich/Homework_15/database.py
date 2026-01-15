import mysql.connector as mysql
from datetime import date
from dateutil.relativedelta import relativedelta


today_new = date.today()
future_date = today_new + relativedelta(months=2)

mydb = mysql.connect(
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    database="st-onl"
)

# Создание таблиц
cursor = mydb.cursor()

query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Tanya2', 'Chishevich2')
cursor.execute(query, values)

new_user_id = cursor.lastrowid # Вот он, ваш ID!
# mydb.commit()
print(new_user_id)

books_data = [
    ('How to Break Web Software 2', new_user_id),
    ('Software Testing Techniques 2', new_user_id),
    ('Agile Testing: A Practical Guide for Testers 2', new_user_id)
]
query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
cursor.executemany(query, books_data)
# mydb.commit()

query = 'INSERT INTO `groups` (title, start_date, end_date)  VALUES (%s, %s, %s)'
cursor.execute(query, ('QA tester 2', today_new, future_date))
group_id = cursor.lastrowid # Вот он, ваш ID!
mydb.commit()

print(group_id)



mydb.close()