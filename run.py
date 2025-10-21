"""
Script para ejecutar la aplicación Reciclapp
"""
import sys
import os

# Agregar el directorio actual al path de Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configurar tamaño de ventana (aspecto smartphone 18:9)
from kivy.core.window import Window
Window.size = (360, 720)  # Smartphone moderno (18:9 aspect ratio - 2:1)

# Importar y ejecutar la aplicación
from app.main import MainApp

if __name__ == '__main__':
    MainApp().run()

