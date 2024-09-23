create database mft;

create table mft.person_tbl(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    password varchar(20),
    email varchar(50),
    number varchar(11)
);