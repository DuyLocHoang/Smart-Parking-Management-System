import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="duyloc",
    database="parking"

)

mycursor = mydb.cursor()


# mycursor.execute("CREATE DATABASE Parking")
# mycursor.execute("CREATE TABLE coordinates (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, cor1 int NOT NULL,cor2 int NOT NULL,"
#                  "cor3 int NOT NULL,cor4 int NOT NULL, slotID int NOT NULL)")
# mycursor.execute("CREATE TABLE states (id int NOT NULL PRIMARY KEY AUTO_INCREMENT,time datetime NOT NULL, state int NOT NULL, slotID int NOT NULL)")

# mycursor.execute("DROP TABLE states ")

def insert_cordb(cor1, cor2, cor3, cor4, slotID):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="duyloc",
        database="parking"

    )
    mycursor = mydb.cursor()

    Q1 = "INSERT INTO coordinates (cor1, cor2, cor3, cor4, slotID) VALUES (%s,%s,%s,%s,%s)"
    val = (cor1, cor2, cor3, cor4, slotID)

    mycursor.execute(Q1, val)
    mydb.commit()
    print(mycursor.rowcount, "slot data inserted.")


def insert_statedb(state, slotID):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="duyloc",
        database="parking"

    )
    mycursor = mydb.cursor()

    Q1 = "INSERT INTO states (time, state, slotID) VALUES (%s,%s,%s)"
    val = (datetime.now(), state, slotID)

    mycursor.execute(Q1, val)
    mydb.commit()
    print(mycursor.rowcount, "state data inserted.")
