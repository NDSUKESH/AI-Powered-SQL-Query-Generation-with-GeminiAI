import sqlite3

##Connect to sqlite3

connection=sqlite3.connect("student.db")

##create a cursor (object) used to etl 
cursor=connection.cursor()


##create table

table="""
Create table student(
name char(30),
class varchar(10),
section varchar(10),
mark int
);
"""

cursor.execute(table)

##add data

cursor.execute('''Insert Into STUDENT values('Sukesh','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Shanthini','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Arvinth','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Bharathi','Devops','A',70)''')
cursor.execute('''Insert Into STUDENT values('Suganthi','HR','A',65)''')
cursor.execute('''Insert Into STUDENT values('Thiraviam','MLOPS','A',55)''')


###cloasss the connection
connection.commit() ##save the data

connection.close()