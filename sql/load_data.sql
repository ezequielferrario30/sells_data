-- Crear la base de datos y usarla
CREATE DATABASE IF NOT EXISTS ventas;
USE ventas;

-- Tabla countries
CREATE TABLE IF NOT EXISTS countries (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(100),
    country_code VARCHAR(10)
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/countries.csv'
INTO TABLE countries
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(country_id, country_name, country_code);

-- Tabla categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(category_id, category_name);

-- Tabla cities
CREATE TABLE IF NOT EXISTS cities (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(100),
    zipcode INT,
    country_id INT
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/cities.csv'
INTO TABLE cities
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(city_id, city_name, zipcode, country_id);

-- Tabla customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    middle_initial CHAR(1),
    last_name VARCHAR(100),
    city_id INT,
    address VARCHAR(255)
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(customer_id, first_name, middle_initial, last_name, city_id, address);

-- Tabla employees
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    middle_initial CHAR(1),
    last_name VARCHAR(100),
    birth_date DATETIME,
    gender CHAR(1),
    city_id INT,
    hire_date DATETIME
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, hire_date);

-- Tabla products
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    price DECIMAL(12,4),
    category_id INT,
    class VARCHAR(50),
    modify_date VARCHAR(50),
    resistant VARCHAR(50),
    is_allergic VARCHAR(50),
    vitality_days INT
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(product_id, product_name, price, category_id, class, modify_date, resistant, is_allergic, vitality_days);

-- Tabla sales
CREATE TABLE IF NOT EXISTS sales (
    sales_id BIGINT PRIMARY KEY,
    sales_person_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    discount DECIMAL(5,2),
    total_price DECIMAL(12,2),
    sales_date VARCHAR(50),
    transaction_number VARCHAR(40)
);

LOAD DATA LOCAL INFILE 'D:/ventas_data_engineering/data/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(sales_id, sales_person_id, customer_id, product_id, quantity, discount, total_price, sales_date, transaction_number);
