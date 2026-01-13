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

cursor = mydb.cursor()
query = 'INSERT INTO `groups` (title, start_date, end_date)  VALUES (%s, %s, %s)'
cursor.execute(query, ('QA tester 2', today_new, future_date))
mydb.commit()



mydb.close()