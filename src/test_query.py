from src.database_sqlalchemy import SQLAlchemyConnection

db = SQLAlchemyConnection()
query = "SELECT * FROM products WHERE price > %s LIMIT 5;"
df = db.execute_query(query, params=(10,))
print(df)

db.close()
