# We use the fetchall() method, which fetches all rows from the last executed statement.

# The fetchone() method will return the first row of the result

# To insert multiple rows into a table, use the executemany() method
# The second parameter of the executemany() method is a list of tuples, containing the data you want to insert

# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword

# You can delete an existing table by using the "DROP TABLE" statement

# You can update existing records in a table by using the "UPDATE" statement:
# "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"


# CREATE DATABASE

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "duyloc",
    database = "parking"

)

mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE Parking")
# mycursor.execute("CREATE TABLE coordinates (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, cor1 int NOT NULL,cor2 int NOT NULL,"
#                  "cor3 int NOT NULL,cor4 int NOT NULL, slotID int NOT NULL)")
# mycursor.execute("CREATE TABLE states (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, state int NOT NULL, slotID int NOT NULL)")
# mycursor.execute("INSERT INTO persons (name,phone) VALUES (%s,%s)",("duyloc", 123))
# mycursor.execute("SELECT * FROM persons WHERE name = 'duyloc'")
# mycursor.execute("ALTER TABLE persons ADD COLUMN age int NOT NULL")
# mycursor.execute("ALTER TABLE persons DROP age")
# print(mycursor.fetchall())
#
# # mycursor.execute("CREATE TABLE persons (name varchar(255) , phone int UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#
# mycursor.execute("CREATE TABLE Adress ( personID int PRIMARY KEY, FOREIGN KEY(personID) REFERENCES persons(personID), address varchar(255))")
#
# Q3 = "INSERT INTO persons(name,phome) VALUES (%s,%s)"
# Q4 = "INSERT INTO Address(address,personID) VALUES (%s,%s)"
#
# for x,person in enumerate(users) :
#     mycursor.execute(Q3,person)
#     last_id = mycursor.lastrowid
#     mycursor.execute(Q4, (last_id,) + user_address[x])
#
# mydb.commit()
#
# mydb.commit()


def insert_db()