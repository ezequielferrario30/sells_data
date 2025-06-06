-- Función: calcular descuento según tipo de cliente
DELIMITER $$
CREATE FUNCTION calcular_descuento(tipo_cliente VARCHAR(20), monto DECIMAL(10,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE descuento DECIMAL(10,2);
    IF tipo_cliente = 'VIP' THEN
        SET descuento = monto * 0.15;
    ELSEIF tipo_cliente = 'Frecuente' THEN
        SET descuento = monto * 0.07;
    ELSE
        SET descuento = monto * 0.02;
    END IF;
    RETURN descuento;
END$$
DELIMITER ;
