import sqlite3

conn = sqlite3.connect('students.db')

cur = conn.cursor()

# представление, содержащее записи одной таблицы, отфильтрованные по какому-либо признаку

cur.execute(""" CREATE VIEW IF NOT EXISTS age_low AS
            SELECT * FROM students
            WHERE students.age < (SELECT AVG(age) FROM students)""")
conn.commit()

cur.execute("SELECT * FROM students")
print(cur.fetchall())

cur.execute("SELECT * FROM age_low")
print(cur.fetchall())

# представление, которое ссылается на другое представление для получения результата;

cur.execute(""" CREATE VIEW IF NOT EXISTS age_low_faculties AS
            SELECT * FROM faculties, age_low
            WHERE faculties.faculty_id = age_low.id_faculty""")
conn.commit()

cur.execute("SELECT DISTINCT * FROM age_low_faculties")
print(cur.fetchall())

# представление, имеющее ограничение на вывод результатов запроса SELECT

cur.execute(""" DROP VIEW IF EXISTS age_low_faculties_lim""")
conn.commit()

cur.execute(""" CREATE VIEW IF NOT EXISTS age_low_faculties_lim AS
            SELECT faculties.faculty_id AS faculties_num, age_low.name AS student_name 
            FROM faculties, age_low
            WHERE faculties.faculty_id = age_low.id_faculty
            LIMIT 10""")
conn.commit()

cur.execute("SELECT DISTINCT * FROM age_low_faculties_lim")
print(cur.fetchall())

# Реализовать триггер INSTEAD OF, который будет менять записи исходной таблицы при попытке обновления записей представления.

cur.execute("DROP TRIGGER IF EXISTS upd_name")
conn.commit()

cur.execute(""" CREATE TRIGGER IF NOT EXISTS upd_name
            INSTEAD OF UPDATE OF student_name
            ON age_low_faculties_lim
            BEGIN
            UPDATE students SET name = NEW.student_name WHERE students.id_faculty = NEW.faculties_num;
            END;""")
conn.commit()

cur.execute("UPDATE age_low_faculties_lim SET student_name = 'Вася' WHERE faculties_num = 4")
conn.commit()

cur.execute("SELECT * FROM age_low_faculties_lim")
print(cur.fetchall())

# Реализовать триггер INSTEAD OF, который будет удалять записи исходной таблицы при попытке удаления записей представления

cur.execute("DROP TRIGGER IF EXISTS del_student")
conn.commit()

cur.execute(""" CREATE TRIGGER IF NOT EXISTS del_student
            INSTEAD OF DELETE
            ON age_low
            BEGIN
            DELETE FROM students WHERE students.student_id = OLD.student_id;
            END;""")
conn.commit()

cur.execute("SELECT * FROM students WHERE student_id = 40")
conn.commit()
print(cur.fetchall())
cur.execute("SELECT * FROM age_low WHERE student_id = 40")
conn.commit()
print(cur.fetchall())
cur.execute("DELETE FROM age_low WHERE student_id = 40")
conn.commit()
cur.execute("SELECT * FROM students WHERE student_id = 40")
conn.commit()
print(cur.fetchall())
cur.execute("SELECT * FROM age_low WHERE student_id = 40")
conn.commit()
print(cur.fetchall())

cur.execute("SELECT * FROM age_low")
print(cur.fetchall())
