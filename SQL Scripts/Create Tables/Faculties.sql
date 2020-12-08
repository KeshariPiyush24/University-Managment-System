CREATE TABLE FACULTIES(Emp_ID NUMERIC(6),Experience NUMERIC(2),Course_ID NUMERIC(6),FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEES(Emp_ID),FOREIGN KEY (Course_ID) REFERENCES COURSES(Course_ID));
insert into FACULTIES values(145623,5,15523);
insert into FACULTIES values(221534,3,23214);
insert into FACULTIES values(325475,2,34785);
insert into FACULTIES values(451326,6,45687);
insert into FACULTIES values(565767,2,56799);
insert into FACULTIES values(625648,3,67815);
insert into FACULTIES values(715689,7,78915);
insert into FACULTIES values(988947,4,98798);
insert into FACULTIES values(111346,2,98798);
insert into FACULTIES values(768565,5,78915);