-- procedimiento almacenado: registrar venta
DELIMITER $$
CREATE PROCEDURE registrar_venta(
    IN p_sales_person_id INT,
    IN p_customer_id INT,
    IN p_product_id INT,
    IN p_quantity INT,
    IN p_discount DECIMAL(5,2),
    IN p_total_price DECIMAL(12,2),
    IN p_sales_date VARCHAR(50),
    IN p_transaction_number VARCHAR(40)
)
BEGIN
    INSERT INTO sales(
        sales_person_id, customer_id, product_id,
        quantity, discount, total_price, sales_date, transaction_number
    ) VALUES (
        p_sales_person_id, p_customer_id, p_product_id,
        p_quantity, p_discount, p_total_price, p_sales_date, p_transaction_number
    );
END$$
DELIMITER ;
