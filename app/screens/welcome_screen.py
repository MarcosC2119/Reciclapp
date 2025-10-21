"""
Pantalla de bienvenida - Primera pantalla de la aplicación
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/welcome_screen.kv')


class WelcomeScreen(MDScreen):
    """Pantalla de bienvenida antes del login"""
    
    def comenzar(self):
        """Navegar a la pantalla de inicio de sesión"""
        print("Botón Comenzar presionado")
        # Navegar a la pantalla de login
        self.manager.current = 'login'

