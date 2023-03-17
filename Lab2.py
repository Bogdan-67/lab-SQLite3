import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("""SELECT * FROM students;""")
print(cur.fetchall())

cur.execute("SELECT * FROM practice")
print(cur.fetchall())

cur.execute("""SELECT * FROM faculties;""")
print(cur.fetchall())

cur.execute("""SELECT Count(student_id) as count, strftime('%m', start_date)
FROM students
LEFT JOIN practice ON student_id=id_student
GROUP BY strftime('%m', start_date)
;""")

data = cur.fetchall()
print(data)

X = []
Y = []
for i in range(1, len(data)):
  Y.append(data[i][0])
  X.append(data[i][1])
print(X, Y)

Y1 = np.full(np.size(Y),np.mean(Y))
print(Y1)

plt.plot(X,Y,'b',linewidth=3)
plt.plot(X,Y1,'r-.', linewidth=1)
plt.show()

cur.execute("""SELECT students_num, faculty_name
FROM faculties
GROUP BY faculty_name; """)

data = cur.fetchall()
print(data)

index = []
nums = []
for i in range(len(data)):
  index.append(data[i][1])
  nums.append(data[i][0])
print(index)

plt.bar(index, nums)
plt.show()

series1 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND strftime('%m', start_date) BETWEEN '0' AND '03'
""")
series1.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND strftime('%m', start_date) BETWEEN '04' AND '06'
""")
series1.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND strftime('%m', start_date) BETWEEN '07' AND '09'
""")
series1.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND strftime('%m', start_date) BETWEEN '10' AND '12'
""")
series1.append(cur.fetchone())
print(series1)

series2 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='IGD' AND strftime('%m', start_date) BETWEEN '0' AND '03'
""")
series2.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='IGD' AND strftime('%m', start_date) BETWEEN '04' AND '06'
""")
series2.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='IGD' AND strftime('%m', start_date) BETWEEN '07' AND '09'
""")
series2.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='IGD' AND strftime('%m', start_date) BETWEEN '10' AND '12'
""")
series2.append(cur.fetchone())
print(series2)

series3 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND strftime('%m', start_date) BETWEEN '0' AND '03'
""")
series3.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND strftime('%m', start_date) BETWEEN '04' AND '06'
""")
series3.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND strftime('%m', start_date) BETWEEN '07' AND '09'
""")
series3.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND strftime('%m', start_date) BETWEEN '10' AND '12'
""")
series3.append(cur.fetchone())
print(series3)

series4 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='BMS' AND strftime('%m', start_date) BETWEEN '0' AND '03'
""")
series4.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='BMS' AND strftime('%m', start_date) BETWEEN '04' AND '06'
""")
series4.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='BMS' AND strftime('%m', start_date) BETWEEN '07' AND '09'
""")
series4.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='BMS' AND strftime('%m', start_date) BETWEEN '10' AND '12'
""")
series4.append(cur.fetchone())
print(series4)

ser1 = []
ser2 = []
ser3 = []
ser4 = []
for i in range(4):
  ser1.append(series1[i][0])
  ser2.append(series2[i][0])
  ser3.append(series3[i][0])
  ser4.append(series4[i][0])
print(ser1, ser2, ser3, ser4)

index = np.arange(4)
plt.title('Соотношение студентов факультетов по кварталам')
plt.bar(index, ser1, color = 'r')
plt.bar(index, ser2, color = 'b', bottom=np.array(ser1))
plt.bar(index, ser3, color = 'g', bottom=(np.array(ser1)+np.array(ser2)))
plt.bar(index, ser4, color = 'm', bottom=(np.array(ser1)+np.array(ser2)+np.array(ser3)))
plt.xticks(index,['1 квартал','2 квартал','3 квартал','4 квартал'])
plt.show()

series1 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND location='Moscow'
""")
series1.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND location='Kazan'
""")
series1.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND location='Tver'
""")
series1.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='SPINTex' AND location='Kaluga'
""")
series1.append(cur.fetchone())
print(series1)

series2 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND location='Moscow'
""")
series2.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND location='Kazan'
""")
series2.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND location='Tver'
""")
series2.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='VMT' AND location='Kaluga'
""")
series2.append(cur.fetchone())
print(series2)

series3 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='LPO' AND location='Moscow'
""")
series3.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='LPO' AND location='Kazan'
""")
series3.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='LPO' AND location='Tver'
""")
series3.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='LPO' AND location='Kaluga'
""")
series3.append(cur.fetchone())
print(series3)

series4 = []
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='NMST' AND location='Moscow'
""")
series4.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='NMST' AND location='Kazan'
""")
series4.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='NMST' AND location='Tver'
""")
series4.append(cur.fetchone())
cur.execute("""SELECT COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE faculty_name='NMST' AND location='Kaluga'
""")
series4.append(cur.fetchone())
print(series4)

ser1 = []
ser2 = []
ser3 = []
ser4 = []
for i in range(4):
  ser1.append(series1[i][0])
  ser2.append(series2[i][0])
  ser3.append(series3[i][0])
  ser4.append(series4[i][0])
print(ser1, ser2, ser3, ser4)

index = np.arange(4)
bw = 0.2
plt.title('Соотношение студентов факультетов по городам', fontsize=14)
plt.bar(index, ser1, bw, color='r')
plt.bar(index+bw, ser2, bw, color='b')
plt.bar(index+2*bw, ser3, bw, color='g')
plt.bar(index+3*bw, ser4, bw, color='m')
plt.xticks(index+2*bw,['Москва','Казань','Тверь','Калуга'])
plt.show()


cur.execute("""SELECT faculty_name, COUNT(id_student)
FROM practice
LEFT JOIN students ON student_id=id_student
LEFT JOIN faculties ON faculty_id=id_faculty
WHERE company_name="Sber"
GROUP BY faculty_name
""")

data = cur.fetchall()
print(data)

labels = []
values = []
for i in range(len(data)):
  labels.append(data[i][0])
  values.append(data[i][1])
print(labels, values)

plt.pie(values, labels=labels)
plt.axis('equal')
plt.show()