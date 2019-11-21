# Link to installing mysql for python https://www.w3schools.com/python/python_mysql_getstarted.asp
# Link to simple select statement in python https://www.w3schools.com/python/python_mysql_select.asp
# Link to download pymysql must pip both versions listed here -> https://pymysql.readthedocs.io/en/latest/user/installation.html
import mysql.connector
import pymysql
import csv
import getpass


user = input("User: ")

pswd = getpass.getpass("Password: ")

database = input("DataBase: ")

mydb = mysql.connector.connect(
    host="cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com",
    # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
    user=user,
    passwd=pswd,
    database=database
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from players")

myresult = mycursor.fetchall()

print(myresult[0])

for x in myresult:
    print(x)

mycursor.close()
mydb.close()


# TEMPORARY FUNCTION - just used to delete the players/teams in the txt file for re-inserting tests
def delete():
    try:
        db = pymysql.connect('cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com',
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             '',
                             '',
                             '',
                             local_infile=True)
        mycursor = db.cursor()
        delete = """DELETE FROM players WHERE PlayerID = 1 or PlayerID = 2 or PlayerID = 3 or PlayerID = 4 or PlayerID = 5"""
        delete2 = """DELETE FROM teams WHERE TeamID = 123451 or TeamID = 789101 or TeamID = 111211 or TeamID = 314151"""
        mycursor.execute(delete)
        mycursor.execute(delete2)
        db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of delete


# singlePlayerInsert
# takes in the file and reads the lines then inserts each one individually
def singlePlayersInsert(path):
    try:
        db = pymysql.connect('cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com',
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             '',
                             '',
                             '',
                             local_infile=True)
        mycursor = db.cursor()
        with open(path, mode='r') as csv_file:

            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                print(row[1])
                print(len(row))
                sql_single_insert = """INSERT INTO players (PlayerID,FirsName,LastName,TeamID,Position,Touchdowns,TotalYards,Salary) VALUES (%s, '%s', '%s', %s, '%s', %s, %s, %s)"""
                insert = sql_single_insert % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                print(insert)
                mycursor.execute(insert)
                db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of singlePlayerInsert


# multInsert
# inserts multiple lines at once in to a given table
def multInsert(path, table):
    try:
        db = pymysql.connect('cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com',
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             '',
                             '',
                             '',
                             local_infile=True)
        mycursor = db.cursor()
        with open(path, mode='r') as csv_file:

            csv_data = csv.reader(csv_file, delimiter=',')
            list_tuples = []
            for row in csv_data:
                list_tuples.append(tuple(row))
            values = ', '.join(map(str, list_tuples))
            print(list_tuples)
            temp = "INSERT INTO %s VALUES {}" % table
            insert = temp.format(values)
            mycursor.execute(insert)
            db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of multInsert


# loadData function
# loads data for any table and inserts
def loadData(path, table):
    try:
        db = pymysql.connect('cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com',
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             '',
                             '',
                             '',
                             local_infile=True)
        mycursor = db.cursor()

        # set local_infile to true just incase its not already
        mycursor.execute("""SET GlOBAL local_infile = 1""")
        db.commit()
        loadDataInsert = """LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'"""
        insertTuple = (path, table)
        mycursor.execute(loadDataInsert % insertTuple)
        db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
# end of loadDataPlayers
