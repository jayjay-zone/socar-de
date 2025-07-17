CREATE TABLE IF NOT EXISTS car_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    brand VARCHAR(255),
    year INT
);

INSERT INTO car_info (name, brand, year)
VALUES ("model3", "Tesla", 2022);