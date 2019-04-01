drop database 2611982589_verk7_user;

create database 2611982589_verk7_user;
use 2611982589_verk7_user;

CREATE TABLE users(
    userID VARCHAR(32) not null,
    nafn varchar(32) NOT NULL,
    email VARCHAR(32) NOT NULL,
    lykil varchar(32) NOT NULL,
    primary key (userID)
);

insert into users (userID, nafn, email, lykil) 
VALUES 
('jói','jóimagnusson','jói@gmail.com', 'hallo');
SELECT * FROM users;
DELETE FROM useres where user = 'admin';