# Link to installing mysql for python https://www.w3schools.com/python/python_mysql_getstarted.asp
# Link to simple select statement in python https://www.w3schools.com/python/python_mysql_select.asp

import mysql.connector

mydb = mysql.connector.connect(
    host="cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com",
    # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
    user="admin",
    passwd="database123",
    database="csproject"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from players")

myresult = mycursor.fetchall()

print(myresult[0])

for x in myresult:
    print(x)

mycursor.close()
mydb.close()


# singleInsertPlayers
# inserts a single line of data for players
def singleInsertPlayers( id, firstName, lastName, teamId, position, touchdowns, totalyards, salary):
    try:
        
        mydb = mysql.connector.connect(
            host="cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com",
            # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
            user="admin",
            passwd="database123",
            database="csproject"
        )

        mycursor = mydb.cursor()
        sql_single_insert = """INSERT INTO players (PlayerID,
                                                    FirsName,
                                                    LastName,
                                                    TeamID,
                                                    Position,
                                                    Touchdowns,
                                                    TotalYards,
                                                    Salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
        insertTuple = ( id, firstName, lastName, teamId, position, touchdowns, totalyards, salary)
        mycursor.execute(sql_single_insert, insertTuple)
        mydb.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    mydb.close()
#### end of singleInsertPlayers
    

# loadDataInsertPlayers
# load data insert from text file for table players
def loadDataInsertPlayers( filePath ):
    try:
        
        mydb = mysql.connector.connect(
            host="cs482project.ct5cpbeyrttk.us-east-1.rds.amazonaws.com",
            # FILL IN VALUES, DO NOT PUSH INTO GITHUB PASSWORD AND USER
            user="admin",
            passwd="database123",
            database="csproject"
        )
        
        mycursor = mydb.cursor()
        loadDataInsert = """LOAD DATA LOCAL INFILE '%s' INTO TABLE players FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'"""
        pathF = (loadDataInsert % filePath)
        mycursor.execute(loadDataInsert % filePath)
        mydb.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySql table{}".format(error))

    mycursor.close()
    mydb.close()
### end of loadDataInsertPlayers



singleInsertPlayers( 1994, 'Billy', 'Bob', 110011, 'RB', 20, 2000, 785000)


#path = input("Enter file path: ")
loadDataInsertPlayers("players.csv")


        
