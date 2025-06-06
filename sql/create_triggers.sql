-- Trigger: aplicar descuento y loguear venta automáticamente
DELIMITER $$
CREATE TRIGGER tr_sales_insert
BEFORE INSERT ON sales
FOR EACH ROW
BEGIN
    -- Asumimos que la tabla customers tiene un campo tipo_cliente
    DECLARE tipo VARCHAR(20);
    SELECT tipo_cliente INTO tipo FROM customers WHERE customer_id = NEW.customer_id;
    SET NEW.discount = calcular_descuento(tipo, NEW.total_price) / NEW.total_price;
    
    INSERT INTO ventas_log(sales_id, descripcion)
    VALUES (NEW.sales_id, CONCAT('Venta registrada para cliente ', NEW.customer_id, ' con descuento aplicado.'));
END$$
DELIMITER ;
