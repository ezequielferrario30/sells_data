-- indice para optimizar busquedas por producto y fecha
CREATE INDEX idx_sales_product_date ON sales(product_id, sales_date);
