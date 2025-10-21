"""
Pantalla de perfil de usuario
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/profile_screen.kv')


class ProfileScreen(MDScreen):
    """Pantalla de perfil del usuario"""
    
    def on_edit_profile(self):
        """Callback para editar perfil"""
        print("Editar perfil presionado")
    
    def go_back(self):
        """Volver a la pantalla anterior"""
        self.manager.current = 'home'

