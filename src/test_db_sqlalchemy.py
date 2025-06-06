from src.database_sqlalchemy import SQLAlchemyConnection
import pandas as pd

db = SQLAlchemyConnection()
engine, session = db.connect()

df = pd.read_sql("SELECT * FROM customers LIMIT 5", con=engine)
print(df)

db.close()
