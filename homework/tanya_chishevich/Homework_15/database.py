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
values = ('Tanya3', 'Chishevich3')
cursor.execute(query, values)
new_user_id = cursor.lastrowid
print(f'ID студента: {new_user_id}')

# Создание нескольких книг
books_data = [
    ('How to Break Web Software 3', new_user_id),
    ('Software Testing Techniques 3', new_user_id),
    ('Agile Testing: A Practical Guide for Testers 3', new_user_id)
]
query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
cursor.executemany(query, books_data)

# Создание группы
query = 'INSERT INTO `groups` (title, start_date, end_date)  VALUES (%s, %s, %s)'
cursor.execute(query, ('QA tester 3', today_new, future_date))
group_id = cursor.lastrowid
print(f'ID группы: {group_id}')

# Определение студента в группу
query = 'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(query, (group_id, new_user_id))

# Создание несколько учебных предметов (subjects)
subjects_data = [
    'Agile testing 3',
    'QA testing 3',
    'Software Test automation 3'
]

subjects_ids = []
for subject_name in subjects_data:
    cursor.execute('INSERT INTO subjects (title) VALUES (%s)', (subject_name,))
    subject_id = cursor.lastrowid
    subjects_ids.append(subject_id)
mydb.commit()
print(f'Получение всех id предметов: {subjects_ids}')

# Создание по два занятия для каждого предмета
lessons_data = [
    ('SCRUM 3', subjects_ids[0]),
    ('Kanban 3', subjects_ids[0]),
    ('Functional testing 3', subjects_ids[1]),
    ('UI/UX 3', subjects_ids[1]),
    ('Auto testing Python 3', subjects_ids[2]),
    ('CI/CD 3', subjects_ids[2])
]
lessons_ids = []
for lesson_name, subj_id in lessons_data:
    cursor.execute('INSERT INTO lessons (title, subject_id) VALUES (%s, %s)', (lesson_name, subj_id))
    lesson_id = cursor.lastrowid
    lessons_ids.append(lesson_id)
mydb.commit()
print(f'Получение всех id занятий: {lessons_ids}')

# Создание оценок для всех наших занятий
marks_data = [
    (5, lessons_ids[0], new_user_id),
    (6, lessons_ids[1], new_user_id),
    (7, lessons_ids[2], new_user_id),
    (8, lessons_ids[3], new_user_id),
    (9, lessons_ids[4], new_user_id),
    (10, lessons_ids[5], new_user_id)
]

query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.executemany(query, marks_data)
mydb.commit()

# Получение оценок
query = 'SELECT * from marks where student_id = %s'
cursor.execute(query, (new_user_id,))
print(f'Получение оценок: {cursor.fetchall()}')

# Получение книг для студента
query = 'SELECT * from books where taken_by_student_id = %s'
cursor.execute(query, (new_user_id,))
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
 WHERE s.id = %s
 ORDER BY m.value DESC
"""

cursor.execute(query, (new_user_id,))
print(f'Вся информация о студенте: {cursor.fetchall()}')

mydb.close()
