import mysql.connector
import getpass
import os

print("Enter field values:")
h = input("host:")
u = input("user:")
p = getpass.getpass(prompt="password:")
mydb = mysql.connector.connect(host=h, user=u, password=p)

mycursor = mydb.cursor()

with open("./SQL Scripts/Create Schema/Schema.sql") as f:
    mycursor.execute(f.read())

for script in os.listdir("./SQL Scripts/Create Tables"):
    with open("./SQL Scripts/Create Tables/"+script) as f:
        mycursor.execute(f.read())