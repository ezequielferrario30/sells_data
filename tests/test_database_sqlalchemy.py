from src.database_sqlalchemy import SQLAlchemyConnection

def test_singleton_connection():
    # aplicamos singleton
    db1 = SQLAlchemyConnection()

    db2 = SQLAlchemyConnection()
    
    assert db1 is db2
