"""
Pantalla de inicio
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/home_screen.kv')


class HomeScreen(MDScreen):
    """Pantalla principal de inicio"""
    
    def on_button_click(self):
        """Callback cuando se presiona el botón"""
        print("¡Botón de inicio presionado!")
    
    def go_to_profile(self):
        """Navegar a la pantalla de perfil"""
        self.manager.current = 'profile'

