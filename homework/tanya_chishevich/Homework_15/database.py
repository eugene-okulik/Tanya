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

# Создание студента
query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Tanya2', 'Chishevich2')
cursor.execute(query, values)
new_user_id = cursor.lastrowid
print(f'ID студента: {new_user_id}')

# Создание нескольких книг
books_data = [
    ('How to Break Web Software 2', new_user_id),
    ('Software Testing Techniques 2', new_user_id),
    ('Agile Testing: A Practical Guide for Testers 2', new_user_id)
]
query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
cursor.executemany(query, books_data)

# Создание группы
query = 'INSERT INTO `groups` (title, start_date, end_date)  VALUES (%s, %s, %s)'
cursor.execute(query, ('QA tester 2', today_new, future_date))
group_id = cursor.lastrowid
print(f'ID группы: {group_id}')

# Определение студента в группу
query = 'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(query, (group_id, new_user_id))

# Создание несколько учебных предметов (subjects)
subjects_data = [
    ('Agile testing 2',),
    ('QA testing 2',),
    ('Software Test automation 2',)
]

query = 'INSERT INTO subjects (title) VALUES (%s)'
cursor.executemany(query, subjects_data)
mydb.commit()

# Получение учебных предметов
subjects = ['Agile testing 2', 'QA testing 2', 'Software Test automation 2']
placeholders = ', '.join(['%s'] * len(subjects))
query = f'SELECT * from subjects where title IN ({placeholders})'
cursor.execute(query, tuple(subjects))

results = cursor.fetchall()
print(f'Получение предметов: {results}')

# Создание по два занятия для каждого предмета
lessons_data = [
    ('SCRUM 2', results[0][0]),
    ('Kanban 2', results[0][0]),
    ('Functional testing 2', results[1][0]),
    ('UI/UX 2', results[1][0]),
    ('Auto testing Python 2', results[2][0]),
    ('CI/CD 2', results[2][0])
]

query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
cursor.executemany(query, lessons_data)
mydb.commit()

# Получение занятий
lessons = ['SCRUM 2', 'Kanban 2', 'Functional testing 2', 'UI/UX 2', 'Auto testing Python 2', 'CI/CD 2']
placeholders = ', '.join(['%s'] * len(lessons))
query = f'SELECT * from lessons where title IN ({placeholders})'
cursor.execute(query, tuple(lessons))

results_lesson = cursor.fetchall()
print(f'Получение занятий: {results_lesson}')

# Создание оценок для всех наших занятий
marks_data = [
    (5, results_lesson[0][0], new_user_id),
    (6, results_lesson[1][0], new_user_id),
    (7, results_lesson[2][0], new_user_id),
    (8, results_lesson[3][0], new_user_id),
    (9, results_lesson[4][0], new_user_id),
    (10, results_lesson[5][0], new_user_id)
]

query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.executemany(query, marks_data)
mydb.commit()

# Получение оценок
cursor.execute(f'SELECT * from marks where student_id = {new_user_id}')
print(f'Получение оценок: {cursor.fetchall()}')

# Получение книг для студента
cursor.execute(f'SELECT * from books where taken_by_student_id = {new_user_id}')
print(f'Получение книг нашего студента: {cursor.fetchall()}')

# Вся информация о студенте
query = f"""
 SELECT 
    s.name,
    s.second_name,
    g.title AS TitleGroups,
    b.title AS TitleBooks,
    l.title,
    m.value 
 FROM students s 
 JOIN `groups` g ON g.id = s.group_id
 JOIN books b ON b.taken_by_student_id = s.id
 JOIN subjects s2
 JOIN lessons l ON l.subject_id = s2.id
 JOIN marks m ON m.student_id = s.id and m.lesson_id = l.id
 WHERE s.id = {new_user_id}
 ORDER BY m.value DESC
"""

cursor.execute(query)
print(f'Вся информация о студенте: {cursor.fetchall()}')

mydb.close()
