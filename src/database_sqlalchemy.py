from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import pandas as pd

class SQLAlchemyConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLAlchemyConnection, cls).__new__(cls)
            cls._instance._engine = None
            cls._instance._session = None
        return cls._instance

    def connect(self):
        if self._engine is None:
            load_dotenv()
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            host = os.getenv("DB_HOST")
            db = os.getenv("DB_NAME")
            port = os.getenv("DB_PORT", "3306")
            connection_str = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
            self._engine = create_engine(connection_str)
            self._session = sessionmaker(bind=self._engine)()
        return self._engine, self._session

    def close(self):
        if self._session:
            self._session.close()
        self._engine = None
        self._session = None

    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta SQL y retorna el resultado como DataFrame de pandas.
        :param query: str, consulta SQL a ejecutar
        :param params: lista de valores para el query (%s)
        :return: pandas.DataFrame con los resultados
        """
        engine, _ = self.connect()
        df = pd.read_sql(query, con=engine, params=params)
        return df
