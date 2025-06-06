-- Vista: ventas mensuales por ciudad y categoría
CREATE OR REPLACE VIEW ventas_mensuales_ciudad_categoria AS
SELECT
    ci.city_name,
    ca.category_name,
    DATE_FORMAT(s.sales_date, '%Y-%m') AS mes,
    SUM(s.total_price) AS total_ventas
FROM
    sales s
    JOIN customers cu ON s.customer_id = cu.customer_id
    JOIN cities ci ON cu.city_id = ci.city_id
    JOIN products p ON s.product_id = p.product_id
    JOIN categories ca ON p.category_id = ca.category_id
GROUP BY ci.city_name, ca.category_name, DATE_FORMAT(s.sales_date, '%Y-%m');
