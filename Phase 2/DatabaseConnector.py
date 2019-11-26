# Link to installing mysql for python https://www.w3schools.com/python/python_mysql_getstarted.asp
# Link to simple select statement in python https://www.w3schools.com/python/python_mysql_select.asp
# Link to download pymysql must pip both versions listed here -> https://pymysql.readthedocs.io/en/latest/user/installation.html
# remote host: cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com
import mysql.connector
import pymysql
import csv


user = ""

host = ""

pswd = ""

database = ""

# mydb = mysql.connector.connect(
#     host="cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com",
#     # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
#     user=user,
#     passwd=pswd,
#     database=database
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * from players")

# myresult = mycursor.fetchall()

# print(myresult[0])

# for x in myresult:
#     print(x)

# mycursor.close()
# mydb.close()


def GetUserInfo(h, u, p, d):
    global user
    global pswd
    global database
    global host

    host = h

    user = u

    pswd = p

    database = d


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
    global host
    global user
    global pswd
    global database

    try:
        db = pymysql.connect(host,
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             user,
                             pswd,
                             database,
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
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             user,
                             pswd,
                             database,
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
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()

        # set local_infile to true just incase its not already
        mycursor.execute("""SET GlOBAL local_infile = 1""")
        db.commit()
        loadDataInsert = """LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'"""
        insertTuple = (path, table)
        print(insertTuple)
        mycursor.execute(loadDataInsert % insertTuple)
        db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
# end of loadDataPlayers

# deleteTableData
# deletes all the data in a table


def deleteTableData(table):
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()

        mycursor.execute("DELETE FROM %s" % table)
        print("Deleted")
        db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
# end of deleteTableData


# average function
# this gives the average of a column in a table. We can assume the column is all integers
def average(table, column):
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()

        mycursor.execute("SELECT avg(%s) from %s" % (column, table))
        db.commit()
        myresult = mycursor.fetchall()
        string = str(myresult[0])
        value = string[10:(len(string)-4)]
        return value

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
# end of average

    # selectDisplay
# takes in a table name and displays data


def selectDisplay(table):
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()

        print("SELECT * from %s" % table)
        mycursor.execute("SELECT * from %s" % table)
        db.commit()
        myresult = mycursor.fetchall()

        print(myresult)
        # Need to fiqure out how to display this on our GUI interface
        return myresult

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
# end of select display
