# Link to installing mysql for python https://www.w3schools.com/python/python_mysql_getstarted.asp
# Link to simple select statement in python https://www.w3schools.com/python/python_mysql_select.asp
# Link to download pymysql must pip both versions listed here -> https://pymysql.readthedocs.io/en/latest/user/installation.html
# remote host: cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com
import mysql.connector
import pymysql
import csv
import time


user = "root"

host = "localhost"

pswd = "Airplanes13!"

database = "cs482_project"

# getUserInfo
# logins into database with info


def getUserInfo(h, u, p, d):
    global user
    global pswd
    global database
    global host

    host = h

    user = u

    pswd = p

    database = d
# end of getuserInfo

# singlePlayerInsert
# takes in the file and reads the lines then inserts each one individually
def singlePlayersInsert(path):
    global host
    global user
    global pswd
    global database

    try:
        db = pymysql.connect(host,
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()
        with open(path, mode='r') as csv_file:

            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                sql_single_insert = """INSERT INTO players (PlayerID,FirsName,LastName,TeamID,Position,Touchdowns,TotalYards,Salary) VALUES (%s, '%s', '%s', %s, '%s', %s, %s, %s)"""
                insert = sql_single_insert % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                mycursor.execute(insert)
                db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of singlePlayerInsert


# singleTeamsInsert
# takes in the file and reads the lines then inserts each one individually
def singleTeamsInsert(path):
    global host
    global user
    global pswd
    global database

    try:
        db = pymysql.connect(host,
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()
        with open(path, mode='r') as csv_file:

            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                sql_single_insert = """INSERT INTO teams (TeamID, TeamName, City) VALUES (%s, '%s', '%s')"""
                insert = sql_single_insert % (row[0], row[1], row[2])
                mycursor.execute(insert)
                db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of singleTeamsInsert

# singlePlayInsert
# takes in the file and reads the lines then inserts each one individually
def singlePlayInsert(path):
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()
        with open(path, mode='r') as csv_file:

            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                sql_single_insert = """INSERT INTO play (PlayerID, GameID) VALUES (%s, %s)"""
                insert = sql_single_insert % (row[0], row[1])
                mycursor.execute(insert)
                db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of singlePlayInsert


# singlePlayInsert
# takes in the file and reads the lines then inserts each one individually
def singleGamesInsert(path):
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()
        with open(path, mode='r') as csv_file:

            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                sql_single_insert = """INSERT INTO games (GameID, Date, Stadium, Result, Attendance, TicketRevenue) VALUES (%s, '%s', '%s', '%s', %s, %s)"""
                insert = sql_single_insert % (row[0], row[1], row[2], row[3], row[4], row[5])
                mycursor.execute(insert)
                db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    db.close()
# end of singlePlayInsert


# multInsert
# inserts multiple lines at once in to a given table
def multInsert(path, table):
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
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
    start_time = time.time()
    global host
    global user
    global pswd
    global database
    try:
        db = pymysql.connect(host,
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
        mycursor.execute(loadDataInsert % insertTuple)
        db.commit()

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
    end_time = time.time()
    return end_time-start_time
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
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()

        mycursor.execute("DELETE FROM %s" % table)
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
                             user,
                             pswd,
                             database,
                             local_infile=True)
        mycursor = db.cursor()

        mycursor.execute("SELECT * from %s" % table)
        db.commit()
        myresult = mycursor.fetchall()
        return myresult

    except pymysql.InternalError as error:
        print("Failed to insert into MySql table{}".format(error))
    mycursor.close()
    db.close()
# end of select display



