"""
Configuración de base de datos MySQL para Reciclapp
"""

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',  # Cambiar por tu servidor MySQL
    'database': 'reciclapp_db',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'port': 3306
}

# Configuración alternativa para desarrollo local
DB_CONFIG_DEV = {
    'host': 'localhost',
    'database': 'reciclapp_dev',
    'user': 'root',
    'password': '',
    'port': 3306
}
