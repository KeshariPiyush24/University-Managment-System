CREATE TABLE STAFFS( Emp_ID NUMERIC(6), Category VARCHAR(255), FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEES(Emp_ID));
insert into STAFFS values(145623,'Carpenter');
insert into STAFFS values(221534,'Plumber');
insert into STAFFS values(715689,'Carpenter');
insert into STAFFS values(988947,'Electrician');
insert into STAFFS values(111346,'Plumber');
insert into STAFFS values(768565,'Electrician');