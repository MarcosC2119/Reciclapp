"""
Script para inicializar la base de datos con usuarios de ejemplo
Ejecutar este script una vez para crear la base de datos y usuarios de prueba
"""
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database.init_data import create_sample_users

if __name__ == "__main__":
    print("Inicializando base de datos de Reciclapp...")
    create_sample_users()
    print("\nBase de datos inicializada correctamente!")
    print("\nUsuarios de prueba creados:")
    print("   - ana_eco / 123456")
    print("   - carlos_green / 123456") 
    print("   - maria_eco / 123456")
    print("\nAhora puedes hacer login en la aplicacion con cualquiera de estos usuarios.")
