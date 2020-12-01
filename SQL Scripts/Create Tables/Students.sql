CREATE TABLE STUDENTS
(
    Student_ID NUMERIC(8) PRIMARY KEY,
    F_NAME VARCHAR(255),
    L_NAME VARCHAR(255),
    Date_Of_Birth DATE,
    Gender CHAR(1),
    Phone NUMERIC(10) UNIQUE ,
    Email VARCHAR(255) UNIQUE,
    House_Number VARCHAR(255),
    City VARCHAR(255),
    Street VARCHAR(255),
    Town VARCHAR(255),
    Semester NUMERIC,
    CPI DECIMAL(3, 2)
);