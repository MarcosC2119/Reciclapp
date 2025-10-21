"""
Aplicación principal KivyMD - Reciclapp
"""
import sys
import os

# Agregar el directorio raíz al path si no está
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from kivymd.app import MDApp
from kivy.lang import Builder
from app.screens.welcome_screen import WelcomeScreen
from app.screens.login_screen import LoginScreen
from app.screens.home_screen import HomeScreen
from app.screens.profile_screen import ProfileScreen


class MainApp(MDApp):
    """Aplicación principal - Reciclapp"""
    
    def build(self):
        """Construye la aplicación"""
        # Configuración del tema
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        
        # Cargar el archivo KV principal
        sm = Builder.load_file('app/main.kv')
        
        # Establecer la pantalla de bienvenida como inicial
        sm.current = 'welcome'
        
        return sm
    
    def switch_screen(self, screen_name):
        """Cambia entre pantallas"""
        self.root.current = screen_name


if __name__ == '__main__':
    MainApp().run()
