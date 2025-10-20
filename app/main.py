"""
Reciclapp - Aplicación principal
Punto de entrada de la aplicación móvil de reciclaje
"""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

# Importar pantallas
from app.screens.login_screen import LoginScreen
from app.screens.home_screen import HomeScreen

class ReciclappApp(MDApp):
    """Aplicación principal de Reciclapp"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Reciclapp"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        
    def build(self):
        """Construir la interfaz de la aplicación"""
        # Configurar tamaño de ventana para desarrollo
        Window.size = (360, 640)  # Tamaño típico de móvil
        
        # Crear el gestor de pantallas
        screen_manager = MDScreenManager()
        
        # Agregar pantallas
        screen_manager.add_widget(LoginScreen(name='login'))
        screen_manager.add_widget(HomeScreen(name='home'))
        
        return screen_manager

if __name__ == '__main__':
    ReciclappApp().run()
