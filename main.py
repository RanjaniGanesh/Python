import mysql.connector

connection = mysql.connector.connect(host="localhost", database="student_mark", user="root", password="")
cursor_object = connection.cursor()
insert_values =("INSERT into student (Name,Mark1,Mark2,Mark3,Mark4,Mark5) values('Hanu','82','76','75','85','87')")
insert_val = ("update student set total= mark1+mark2+mark3+mark4+mark5, average = (mark1+mark2+mark3+mark4+mark5)/5")
cursor_object.execute(insert_values)
cursor_object.execute(insert_val)
connection.commit()
cursor_object.execute("SELECT * from student")
result =cursor_object.fetchall()

print(cursor_object.rowcount,"value inserted")
#print(result)
for i in result:
    print(i)

