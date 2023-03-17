import sqlite3
import random
import names
from datetime import date
from dateutil.relativedelta import relativedelta

conn = sqlite3.connect('students.db')

cur = conn.cursor()

cur.execute(""" DROP TABLE IF EXISTS faculties; """)
conn.commit()

cur.execute(""" DROP TABLE IF EXISTS students; """)
conn.commit()

cur.execute(""" DROP TABLE IF EXISTS practice; """)
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS faculties(
   faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
   faculty_name TEXT NOT NULL,
   students_num INTEGER NOT NULL DEFAULT 0,
   teachers_num INTEGER NOT NULL);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
   student_id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   surname TEXT NOT NULL,
   age INTEGER NOT NULL,
   date_birth DATE NOT NULL,
   id_faculty INTEGER NOT NULL,
   FOREIGN KEY (id_faculty) REFERENCES faculties(faculty_id));
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS practice(
   practice_id INTEGER PRIMARY KEY AUTOINCREMENT,
   company_name TEXT NOT NULL,
   location TEXT NOT NULL,
   start_date DATE NOT NULL,
   finish_date DATE NOT NULL,
   id_student INTEGER NOT NULL,
   FOREIGN KEY (id_student) REFERENCES students(student_id));
""")
conn.commit()


first_date_birth = date(year = 1999, month = 1, day = 1).toordinal()
last_date_birth = date(year = 2002, month = 12, day = 31).toordinal()


companies = ['Sber', 'Yandex', 'VK', 'Mail.ru', 'Tinkoff', 'Gazprom', 'Google', 'Microsoft']

location = ['Moscow', 'Saint-Petersburg', 'Kazan', 'Tver', 'Kaluga', 'Ryazan', 'Krasnodar', 'Vladimir', 'Tula']

cur.execute("PRAGMA foreign_keys=ON")
conn.commit()

faculties = ['SPINTex', 'MPSU', 'VMT', 'MiUP', 'IGD', 'NMST', 'BMS', 'LPO']

faculty = list()
for i in range(8):
    fct = (faculties[i], random.randint(20, 40))
    faculty.append(fct)

cur.executemany("INSERT INTO faculties(faculty_name, teachers_num) VALUES (?,?)", faculty)
conn.commit()

student = list()
for i in range(10000):
    date_birth = date.fromordinal(random.randint(first_date_birth, last_date_birth))
    tup = (names.get_first_name(), names.get_last_name(), relativedelta(date.today(), date_birth).years, date_birth, random.randint(1, 8))
    student.append(tup)

cur.executemany("INSERT INTO students(name, surname, age, date_birth, id_faculty) VALUES (?,?,?,?,?)", student)
conn.commit()

cur.execute(""" UPDATE faculties SET students_num = (SELECT COUNT(*) FROM students WHERE students.id_faculty=faculties.faculty_id) """)
conn.commit()

first_date = date(year = 2023, month = 1, day = 1).toordinal()
last_date = date(year = 2023, month = 12, day = 31).toordinal()

practices = list()
for i in range(10000):
    start_date = date.fromordinal(random.randint(first_date, last_date))
    finish_date = date.fromordinal(start_date.toordinal() + 90)
    cur.execute("INSERT INTO practice(company_name, location, start_date, finish_date, id_student) VALUES (?,?,?,?,?)", (companies[random.randint(0, 7)], location[random.randint(0, 8)], start_date, finish_date, i+1))

conn.commit()

cur.execute("SELECT * FROM students")
print(cur.fetchmany(5))

cur.execute("SELECT * FROM faculties")
print(cur.fetchmany(8))

cur.execute("SELECT * FROM practice")
print(cur.fetchmany(5))

conn.close()
