import pytest
from sqlalchemy import text
from src.database_sqlalchemy import SQLAlchemyConnection

@pytest.mark.integration
def test_registro_venta_y_log():
    db = SQLAlchemyConnection()
    engine, session = db.connect()

    # 1. Insertar venta usando el procedimiento almacenado
    # Usamos IDs altos para evitar colisiones en tests repetidos
    venta_data = {
        "a": 1,  # sales_person_id
        "b": 1,  # customer_id
        "c": 1,  # product_id
        "d": 2,  # quantity
        "e": 0.05,  # discount
        "f": 200,   # total_price
        "g": '2024-06-10',
        "h": 'T2024061001'
    }
    session.execute(
        text("CALL registrar_venta(:a, :b, :c, :d, :e, :f, :g, :h);"),
        venta_data
    )
    session.commit()

    # 2. Verificar que la venta fue insertada
    query_venta = "SELECT * FROM sales WHERE transaction_number = 'T2024061001';"
    df_venta = db.execute_query(query_venta)
    assert not df_venta.empty, "La venta no fue registrada por el procedimiento."

    # 3. Verificar que el trigger generó un log en ventas_log
    query_log = "SELECT * FROM ventas_log WHERE sales_id = %s ORDER BY log_id DESC LIMIT 1;" % df_venta.iloc[0]['sales_id']
    df_log = db.execute_query(query_log)
    assert not df_log.empty, "El trigger no generó un log para la venta."

    # 4. (Opcional) Verificar el descuento aplicado usando la función SQL
    # Ejemplo para un cliente VIP
    query_func = "SELECT calcular_descuento('VIP', 200) AS descuento;"
    df_func = db.execute_query(query_func)
    assert round(float(df_func.iloc[0]['descuento']), 2) == 30.00, "La función de descuento no devolvió el valor esperado."

    db.close()
