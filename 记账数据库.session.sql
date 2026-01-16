USE finance_db;
CREATE Table transactions(
    id BIGINT PRIMARY key auto_increment,
    user_id int not NULL,
    date DATE not NULL,
    account VARCHAR(50) NOT NULL,
    type ENUM('income','expense') NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount DECIMAL(12,2) NOT NULL check (amount > 0),
    direction TINYINT NOT NULL check (direction in (1,-1)),
    created_at datetime DEFAULT current_timestamp,
    FOREIGN key (user_id) REFERENCES users(id) on delete CASCADE
);
