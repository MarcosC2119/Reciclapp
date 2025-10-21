"""
Pantalla de Comunidad - Reciclapp
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/community_screen.kv')


class CommunityScreen(MDScreen):
    """Pantalla de comunidad para conectar con otros usuarios"""

    def navegar_home(self):
        """Navega a la pantalla de inicio"""
        print("Navegando a Home desde Comunidad")
        self.manager.current = 'home'

    def navegar_logros(self):
        """Navega a la pantalla de logros"""
        print("Navegando a Logros desde Comunidad")
        # self.manager.current = 'logros'  # Descomentar cuando esté lista

    def navegar_perfil(self):
        """Navega a la pantalla de perfil"""
        print("Navegando a Perfil desde Comunidad")
        self.manager.current = 'profile'

    def escanear_qr(self):
        """Maneja la acción de escanear QR"""
        print("Escanear QR presionado desde Comunidad")
        # Implementar lógica de escaneo QR

