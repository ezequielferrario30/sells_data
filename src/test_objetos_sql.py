from src.database_sqlalchemy import SQLAlchemyConnection
from sqlalchemy import text

db = SQLAlchemyConnection()

# 1. Llamar a la función SQL 'calcular_descuento'
print("1) Llamando a la función SQL 'calcular_descuento':")
query_func = "SELECT calcular_descuento('VIP', 500) AS descuento;"
df_func = db.execute_query(query_func)
print(df_func)
print()

# 2. Consultar la vista de ventas mensuales por ciudad y categoría
print("2) Consultando la vista 'ventas_mensuales_ciudad_categoria':")
query_vista = "SELECT * FROM ventas_mensuales_ciudad_categoria LIMIT 5;"
df_vista = db.execute_query(query_vista)
print(df_vista)
print()

# 3. Llamar al procedimiento almacenado 'registrar_venta'
print("3) Llamando al procedimiento almacenado 'registrar_venta':")
engine, session = db.connect()
try:
    session.execute(
        text("CALL registrar_venta(:a, :b, :c, :d, :e, :f, :g, :h);"),
        {
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 2,
            "e": 0.05,
            "f": 200,
            "g": '2024-06-10',
            "h": 'T2024061001'
        }
    )
    session.commit()
    # Verificar la venta insertada
    query_venta = "SELECT * FROM sales ORDER BY sales_id DESC LIMIT 1;"
    df_venta = db.execute_query(query_venta)
    print("Venta registrada por el procedimiento:")
    print(df_venta)
except Exception as e:
    print("Error al llamar al procedimiento almacenado:", e)
print()

# 4. Consultar los logs generados por trigger
print("4) Logs de ventas generados por trigger (tabla ventas_log):")
query_log = "SELECT * FROM ventas_log ORDER BY log_id DESC LIMIT 5;"
df_log = db.execute_query(query_log)
print(df_log)
print()

# 5. Mostrar índices creados en la tabla sales
print("5) Índices de la tabla 'sales':")
query_idx = "SHOW INDEX FROM sales;"
df_idx = db.execute_query(query_idx)
print(df_idx)
print()

db.close()
