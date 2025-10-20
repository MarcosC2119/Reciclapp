"""
Configuración de base de datos MySQL
Conexión y configuración de la base de datos
"""

import mysql.connector
from mysql.connector import Error
from config.database_config import DB_CONFIG

class DatabaseConnection:
    """Manejo de conexión a la base de datos MySQL"""
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establecer conexión con la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=DB_CONFIG['host'],
                database=DB_CONFIG['database'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                port=DB_CONFIG['port']
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Conexión exitosa a MySQL")
                return True
                
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return False
    
    def disconnect(self):
        """Cerrar conexión con la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión MySQL cerrada")
    
    def execute_query(self, query, params=None):
        """Ejecutar consulta SQL"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor.rowcount
                
        except Error as e:
            print(f"Error ejecutando consulta: {e}")
            return None
