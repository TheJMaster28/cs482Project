# Link to installing mysql for python https://www.w3schools.com/python/python_mysql_getstarted.asp
# Link to simple select statement in python https://www.w3schools.com/python/python_mysql_select.asp

import mysql.connector

mydb = mysql.connector.connect(
    host="cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com",
    # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
    user="",
    passwd="",
    database="csproject"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from players")

myresult = mycursor.fetchall()

print(myresult[0])

for x in myresult:
    print(x)
