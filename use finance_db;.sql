use finance_db;
CREATE USER 'finance_user'@'localhost' IDENTIFIED BY 'cwb&hyd20010915';
GRANT ALL PRIVILEGES ON finance_db.* TO 'finance_user'@'localhost';


FLUSH PRIVILEGES;
