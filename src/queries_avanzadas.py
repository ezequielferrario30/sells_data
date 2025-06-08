from src.database_sqlalchemy import SQLAlchemyConnection

# Crear la instancia Singleton de conexión
db = SQLAlchemyConnection()


# Top 10 clientes por compras totales (CTE + RANK)

query1 = """
WITH compras_por_cliente AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        SUM(s.total_price) AS total_gastado
    FROM
        customers c
        JOIN sales s ON c.customer_id = s.customer_id
    GROUP BY
        c.customer_id, c.first_name, c.last_name
)
SELECT
    *,
    RANK() OVER (ORDER BY total_gastado DESC) AS ranking
FROM compras_por_cliente
ORDER BY total_gastado DESC
LIMIT 10;
"""
df1 = db.execute_query(query1)
print("------ Top 10 clientes por compras totales ------")
print(df1)
print()


# ventas de productos con ROW_NUMBER por fecha de venta

query2 = """
WITH ventas_productos AS (
    SELECT
        p.product_id,
        p.product_name,
        s.sales_date,
        s.total_price
    FROM
        products p
        JOIN sales s ON p.product_id = s.product_id
)
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY sales_date DESC) AS venta_reciente
FROM ventas_productos
ORDER BY product_id, sales_date DESC;
"""
df2 = db.execute_query(query2)
print("------ Ventas de productos con ROW_NUMBER ------")
print(df2.head(20))
print()


#  rank de productos más vendidos por cantidad (DENSE_RANK)

query3 = """
WITH ventas_por_producto AS (
    SELECT
        p.product_id,
        p.product_name,
        SUM(s.quantity) AS total_vendido
    FROM
        products p
        JOIN sales s ON p.product_id = s.product_id
    GROUP BY
        p.product_id, p.product_name
)
SELECT
    *,
    DENSE_RANK() OVER (ORDER BY total_vendido DESC) AS ranking
FROM ventas_por_producto
ORDER BY total_vendido DESC
LIMIT 10;
"""
df3 = db.execute_query(query3)
print("------ Top 10 productos más vendidos ------")
print(df3)
print()


# 4. evolucionmensual de ventas (CTE + SUM acumulado)

query4 = """
WITH ventas_mensuales AS (
    SELECT
        DATE_FORMAT(s.sales_date, '%Y-%m') AS mes,
        SUM(s.total_price) AS total_mes
    FROM sales s
    GROUP BY DATE_FORMAT(s.sales_date, '%Y-%m')
)
SELECT
    mes,
    total_mes,
    SUM(total_mes) OVER (ORDER BY mes) AS acumulado
FROM ventas_mensuales
ORDER BY mes;
"""
df4 = db.execute_query(query4)
print("------ Evolución mensual de ventas ------")
print(df4)
print()


# clientes frecuentes en cada ciudad (RANK PARTITION BY city)

query5 = """
WITH clientes_ciudad AS (
    SELECT
        c.city_id,
        c.customer_id,
        c.first_name,
        c.last_name,
        COUNT(s.sales_id) AS cantidad_compras
    FROM customers c
    JOIN sales s ON c.customer_id = s.customer_id
    GROUP BY c.city_id, c.customer_id, c.first_name, c.last_name
)
SELECT
    *,
    RANK() OVER (PARTITION BY city_id ORDER BY cantidad_compras DESC) AS ranking_en_ciudad
FROM clientes_ciudad
WHERE cantidad_compras > 0
ORDER BY city_id, ranking_en_ciudad
LIMIT 50;
"""
df5 = db.execute_query(query5)
print("------ Top clientes frecuentes por ciudad ------")
print(df5)
print()


# venta por categoría y su ranking mensual (RANK, partición por mes)

query6 = """
WITH ventas_categoria_mes AS (
    SELECT
        cat.category_name,
        DATE_FORMAT(s.sales_date, '%Y-%m') AS mes,
        SUM(s.total_price) AS total_categoria_mes
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    JOIN categories cat ON p.category_id = cat.category_id
    GROUP BY cat.category_name, DATE_FORMAT(s.sales_date, '%Y-%m')
)
SELECT
    *,
    RANK() OVER (PARTITION BY mes ORDER BY total_categoria_mes DESC) AS ranking_categoria_mes
FROM ventas_categoria_mes
ORDER BY mes, ranking_categoria_mes;
"""
df6 = db.execute_query(query6)
print("------ Ventas por categoría y ranking mensual ------")
print(df6)
print()


db.close()
