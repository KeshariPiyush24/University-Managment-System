CREATE TABLE STUDENTS
(
    SID NUMERIC(8) PRIMARY KEY,
    F_NAME VARCHAR(255),
    L_NAME VARCHAR(255),
    FATHER_NAME VARCHAR(255) NOT NULL,
    DOB DATE NOT NULL,
    EMAIL VARCHAR(255) NOT NULL UNIQUE,
    ADDRESS VARCHAR(255) NOT NULL,
    PHONE_NO NUMERIC(10) NOT NULL UNIQUE ,
    X_PERCENTAGE DECIMAL(5,2) NOT NULL,
    XII_PERCENTAGE DECIMAL(5,2) NOT NULL,
    YEAR NUMERIC
);