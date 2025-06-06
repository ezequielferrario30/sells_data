from src.database_sqlalchemy import SQLAlchemyConnection

def test_singleton_connection():
    # Instancia 1
    db1 = SQLAlchemyConnection()
    # Instancia 2
    db2 = SQLAlchemyConnection()
    # Deben ser exactamente el mismo objeto (Singleton)
    assert db1 is db2
