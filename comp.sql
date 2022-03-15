#create database company;

use company;

#create table job(job_id int(10) primary key, job_title varchar(15), min_sal int(10), max_sal int(10));

#create table region(region_id int(10) primary key, region_name varchar(15));

#create table country(country_id int(10) primary key, country_name varchar(15), region_id int(10), foreign key(region_id) references region(region_id));

#create table locations(location_id int(10) primary key, street_address varchar(15), postal_code int(10), city varchar(15),state_province varchar(15),country_id int(10),foreign key(country_id) references country(country_id));

#create table department(department_id int(10) primary key, dept_name varchar(15), location_id int(10),foreign key(location_id) references locations(location_id));

#create table employees(employee_id int(10) primary key, first_name varchar(15), last_name varchar(15), email varchar(25), phone_number int(11), hire_date date, job_id int(10), foreign key(job_id) references job(job_id), salary int(10), manager_id int(10),department_id int(10), foreign key(department_id) references department(department_id));

#create table dependents(dependent_id int(10) primary key, first_name varchar(15), last_name varchar(15),relationship varchar(10), employee_id int(10),foreign key(employee_id) references employees(employee_id));

#alter table employees add foreign key(manager_id) references employees(employee_id);

#alter table employees modify column job_id int(10) not null;

#alter table dependents modify column employee_id int(10) not null;

#alter table country modify column region_id int(10) not null;

#alter table locations modify column country_id int(10) not null;

