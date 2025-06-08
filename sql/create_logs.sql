-- tabla de logs para auditoría de ventas (opcional)
CREATE TABLE IF NOT EXISTS ventas_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    sales_id BIGINT,
    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descripcion VARCHAR(255)
);
