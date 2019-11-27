import DatabaseConnector as db

host = input("Host: ")
user = input("User: ")
pwsd = input("Password: ")
schema = input("Schema: ")

db.getUserInfo(host, user, pwsd, schema)
db.deleteTableData("Players")
print(db.loadData(
    "/mnt/d/Documents/NMSU/CS482/cs482Project/Phase 2/Players1000000.txt", "players"))
