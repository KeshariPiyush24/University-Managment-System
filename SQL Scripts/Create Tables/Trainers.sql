CREATE TABLE TRAINERS(Emp_ID NUMERIC(6), Specialization VARCHAR(255), FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEES(Emp_ID));
insert into TRAINERS values(145623,'Computer Science');
insert into TRAINERS values(221534,'Cloud Computing');
insert into TRAINERS values(111346,'Computer Science');
insert into TRAINERS values(768565,'Robotics');