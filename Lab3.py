import sqlite3

conn = sqlite3.connect('students.db')

cur = conn.cursor()

cur.execute(""" DROP TABLE IF EXISTS log_In_students""")
cur.execute("DROP TRIGGER IF EXISTS log_In_stud")
conn.commit()

# Триггер на добавление данных

cur.execute(""" CREATE TABLE IF NOT EXISTS log_In_students(
            Id_stud INTEGER NOT NULL,
            date TEXT NOT NULL)""")
conn.commit()

cur.execute(""" CREATE TRIGGER log_In_stud AFTER INSERT
            ON students
            BEGIN
            INSERT INTO log_In_students(Id_stud, date) VALUES (NEW.student_id, datetime('now'));
            END;""")
conn.commit()

cur.execute("INSERT INTO students(name, surname, age, date_birth, id_faculty) VALUES ('AAA','BBB',123, datetime('now'), 1);")
conn.commit()
cur.execute("SELECT * FROM log_In_students")
print(cur.fetchall())

# Триггер на удаление данных

cur.execute(""" CREATE TABLE IF NOT EXISTS log_Del_students(
            Id_stud INTEGER NOT NULL,
            date TEXT NOT NULL)""")
conn.commit()

cur.execute(""" CREATE TRIGGER IF NOT EXISTS log_Del_stud AFTER DELETE
            ON students
            BEGIN
            INSERT INTO log_Del_students(Id_stud, date) VALUES (OLD.student_id, datetime('now'));
            END;""")
conn.commit()

cur.execute("DELETE FROM students WHERE student_id = 10001;")
conn.commit()
cur.execute("SELECT * FROM log_Del_students")
print(cur.fetchall())

# Триггер на обновление данных

cur.execute("DROP TRIGGER IF EXISTS log_Upd")
cur.execute("DROP TRIGGER IF EXISTS log_UpdLoc")
cur.execute("DROP TABLE IF EXISTS log_Upd_practice")
conn.commit()

cur.execute(""" CREATE TABLE IF NOT EXISTS log_Upd_practice(
            Id_practice INTEGER NOT NULL,
            old_location TEXT NOT NULL,
            new_location TEXT NOT NULL,
            trig_type TEXT)""")
conn.commit()

cur.execute(""" CREATE TRIGGER IF NOT EXISTS log_Upd AFTER UPDATE
            ON practice
            BEGIN
            INSERT INTO log_Upd_practice(Id_practice, old_location, new_location, trig_type) VALUES (OLD.practice_id, OLD.location, NEW.location, 'any update');
            END;""")
conn.commit()

cur.execute(""" CREATE TRIGGER IF NOT EXISTS log_UpdLoc AFTER UPDATE
            OF location
            ON practice
            BEGIN
            INSERT INTO log_Upd_practice(Id_practice, old_location, new_location, trig_type) VALUES (OLD.practice_id, OLD.location, NEW.location, 'location_update');
            END;""")
conn.commit()

cur.execute("""UPDATE practice SET location = "Moscow" 
            WHERE practice_id = 5;""")
cur.execute("""UPDATE practice SET company_name = "Sber" 
            WHERE practice_id = 6;""")
conn.commit()
cur.execute("SELECT * FROM log_Upd_practice")
print(cur.fetchall())

# Триггер на выполнение определенного условия

cur.execute(""" CREATE TABLE IF NOT EXISTS log_Upd_faculties(
            Id_faculty INTEGER NOT NULL,
            old_teachers_num TEXT NOT NULL,
            new_teachers_num TEXT NOT NULL,
            trig_type TEXT)""")
conn.commit()

cur.execute(""" CREATE TRIGGER IF NOT EXISTS log_UpdCondition AFTER UPDATE
            ON faculties WHEN (OLD.teachers_num - NEW.teachers_num) > 0
            BEGIN
            INSERT INTO log_Upd_faculties(Id_faculty, old_teachers_num, new_teachers_num, trig_type) VALUES (OLD.faculty_id, OLD.teachers_num, NEW.teachers_num, 'condition_update');
            END;""")
            
cur.execute("""UPDATE faculties SET teachers_num = teachers_num-1 
            WHERE teachers_num > 30;""")
conn.commit()

cur.execute("SELECT * FROM log_Upd_faculties")
print(cur.fetchall())
