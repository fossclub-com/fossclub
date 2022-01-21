--Run this as the main postgres user

CREATE USER fossclub WITH ENCRYPTED PASSWORD 'fossclub';
CREATE DATABASE fossclub_db WITH OWNER fossclub;
