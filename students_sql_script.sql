drop database if exists students;
create database students;

use students;

drop table if exists student;

create table student
(
    uni            varchar(10) not null
        primary key,
    first_name     varchar(32) not null,
    last_name      varchar(32) not null,
    nationality    varchar(64) not null,
    ethnicity      varchar(32) null,
    gender         varchar(32) null,
    admission_date varchar(64) not null
);