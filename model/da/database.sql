create database book;

create table book.library_tbl(
    id int primary key auto_increment,
    title varchar(30),
    author varchar(30),
    isbn varchar(20),
    language varchar(50),
    genre varchar(11),
    in_out int
);