import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        if self._connection is None or not self._connection.is_connected():
            load_dotenv()  # Carga las variables de entorno
            try:
                self._connection = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME"),
                    auth_plugin='mysql_native_password'
                )
            except Error as e:
                print(f"Error conectando a la base de datos: {e}")
                self._connection = None
        return self._connection

    def close(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            self._connection = None
