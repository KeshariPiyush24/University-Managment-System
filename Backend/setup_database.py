import mysql.connector
import os
import re

c = [re.findall(r".*='(.*)'.?", line) for line in open('Backend\config.txt')]
h = c[0][0]
u = c[1][0]
p = c[2][0]


def create_schema():
    mydb = mysql.connector.connect(host=h, user=u, password=p)
    mycursor = mydb.cursor()
    mycursor.execute("DROP SCHEMA IF EXISTS ums;")
    f = open("./SQL Scripts/Create Schema/Schema.sql")
    mycursor.execute(f.read())
    f.close()
    print("Successfully created schema.......:)\n")
    mycursor.close()


non_dependent_entity = ["Students", "Courses",
                        "Clubs", "Departments", "Login"]
dependent_entity = [script for script in [x.replace(".sql", "") for x in os.listdir(
    "./SQL Scripts/Create Tables")] if script not in non_dependent_entity]
dependent_entity.sort()


def create_non_dependent_tables():
    mydb = mysql.connector.connect(
        host=h, user=u, password=p, database="ums")
    mycursor = mydb.cursor()
    for script in non_dependent_entity:
        with open("./SQL Scripts/Create Tables/"+script+".sql") as f:
            print(f"Creating {script} table...")
            mycursor.execute(f.read())
            print(f"successfully created {script} table.......:)\n")
    mycursor.close()
    print("Completed successfully")


def create_dependent_tables():
    mydb = mysql.connector.connect(
        host=h, user=u, password=p, database="ums")
    mycursor = mydb.cursor()
    for script in dependent_entity:
        with open("./SQL Scripts/Create Tables/"+script+".sql") as f:
            print(f"Creating {script} table...")
            mydb.cursor().execute(f.read())
            print(f"successfully created {script} table.......:)\n")
    mycursor.close()
    print("Completed successfully")


if __name__ == '__main__':
    create_schema()
    create_non_dependent_tables()
    create_dependent_tables()
