import mysql.connector
import os
import re

c = [re.findall(r".*='(.*)'.?", line) for line in open('config.txt')]
h = c[0][0]
u = c[1][0]
p = c[2][0]


def create_schema():
    mydb = mysql.connector.connect(host=h, user=u, password=p)
    mycursor = mydb.cursor()
    mycursor.execute("DROP SCHEMA IF EXISTS ums;")
    f = open("./SQL Scripts/Create Schema/Schema.sql")
    mycursor.execute(f.read(), multi=True)
    f.close()
    print("Successfully created schema.......:)\n")
    mycursor.close()


non_dependent_entity = ["Students", "Courses", "Clubs", "Departments"]

dependent_entity = [script for script in [x.replace(".sql", "") for x in os.listdir(
    "./SQL Scripts/Create Tables")] if script not in non_dependent_entity]

relations = os.listdir("./SQL Scripts/Create Relationships")
dependent_entity.sort()


def create_non_dependent_tables():
    for script in non_dependent_entity:
        with open("./SQL Scripts/Create Tables/"+script+".sql") as f:
            print(f"Creating {script} table...")
            for line in f.readlines():
                mydb = mysql.connector.connect(
                    host=h, user=u, password=p, database="ums")
                mycursor = mydb.cursor()
                mycursor.execute(line)
                mydb.commit()
                mycursor.close()
            print(f"successfully created {script} table.......:)\n")
    print("Completed successfully\n")


def create_dependent_tables():
    for script in dependent_entity:
        with open("./SQL Scripts/Create Tables/"+script+".sql") as f:
            print(f"Creating {script} table...")
            for line in f.readlines():
                mydb = mysql.connector.connect(
                    host=h, user=u, password=p, database="ums")
                mycursor = mydb.cursor()
                mycursor.execute(line)
                mydb.commit()
                mycursor.close()
            print(f"successfully created {script} table.......:)\n")
    print("Completed successfully\n")


def create_relation_tables():
    for script in relations:
        mydb = mysql.connector.connect(
            host=h, user=u, password=p, database="ums")
        mycursor = mydb.cursor()
        print(f"Creating {script} table...")
        with open("./SQL Scripts/Create Relationships/"+script) as f:
            mycursor.execute(f.read(), multi=True)
        print(f"successfully created {script} table.......:)\n")
        mycursor.close()
    print("Completed successfully\n")


if __name__ == '__main__':
    create_schema()
    create_non_dependent_tables()
    create_dependent_tables()
    create_relation_tables()
