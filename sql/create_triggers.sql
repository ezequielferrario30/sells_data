

--  BEFORE INSERT calcula el descuento antes de insertar la venta
DROP TRIGGER IF EXISTS tr_sales_calcular_descuento;
DELIMITER $$
CREATE TRIGGER tr_sales_calcular_descuento
BEFORE INSERT ON sales
FOR EACH ROW
BEGIN
    DECLARE tipo VARCHAR(20);
    SELECT tipo_cliente INTO tipo FROM customers WHERE customer_id = NEW.customer_id;
    SET NEW.discount = calcular_descuento(tipo, NEW.total_price) / NEW.total_price;
END$$
DELIMITER ;

-- 2. AFTER INSERT loguea la venta recién registrada
DROP TRIGGER IF EXISTS tr_sales_log;
DELIMITER $$
CREATE TRIGGER tr_sales_log
AFTER INSERT ON sales
FOR EACH ROW
BEGIN
    INSERT INTO ventas_log(sales_id, descripcion)
    VALUES (NEW.sales_id, CONCAT('Venta registrada para cliente ', NEW.customer_id, ' con descuento aplicado.'));
END$$
DELIMITER ;
