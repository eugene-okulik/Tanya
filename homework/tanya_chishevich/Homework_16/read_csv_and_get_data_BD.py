import csv
import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

mydb = mysql.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME')
)

cursor = mydb.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data_from_csv = list(file_data)

    data = []
    for row in data_from_csv:
        name = row.get('name')
        second_name = row.get('second_name')
        group_title = row.get('group_title')
        book_title = row.get('book_title')
        subject_title = row.get('book_title')
        lesson_title = row.get('book_title')
        mark_value = row.get('mark_value')

        query = """
             SELECT
                s.name,
                s.second_name,
                g.title AS TitleGroups,
                b.title AS TitleBooks,
                s2.title AS TitleSubject,
                l.title AS TitleLessons,
                m.value
             FROM students s
             JOIN `groups` g ON g.id = s.group_id
             JOIN books b ON b.taken_by_student_id = s.id
             JOIN subjects s2
             JOIN lessons l ON l.subject_id = s2.id
             JOIN marks m ON m.student_id = s.id and m.lesson_id = l.id
             WHERE s.name = %s and s.second_name = %s and g.title = %s and b.title = %s
             ORDER BY m.value DESC
            """

        cursor.execute(query, (name, second_name, group_title, book_title))
        result = cursor.fetchall()

        if result:
            print(f'Данные из БД файла {result}')
        else:
            data.append(row)

    for row in data:
        print(f'Данные из csv файла {row}')


mydb.close()
