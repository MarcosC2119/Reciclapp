"""
Script para ejecutar la aplicación Reciclapp
"""
import sys
import os

# Agregar el directorio actual al path de Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar y ejecutar la aplicación
from app.main import MainApp

if __name__ == '__main__':
    MainApp().run()

