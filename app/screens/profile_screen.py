"""
Pantalla de Perfil
Muestra información del usuario, estadísticas, logros y configuración
"""

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño de esta pantalla
Builder.load_file('app/screens/profile_screen.kv')


class ProfileScreen(MDScreen):
    """
    Pantalla que muestra el perfil del usuario con:
    - Información personal
    - Estadísticas de reciclaje
    - Logros recientes
    - Configuración de la aplicación
    """
    
    def volver_home(self):
        """Navega de vuelta a la pantalla de inicio"""
        print("Volver a home desde perfil")
        self.manager.current = 'home'
    
    def cerrar_sesion(self):
        """Cierra la sesión del usuario"""
        print("Cerrando sesión...")
        # Aquí se implementaría la lógica de cierre de sesión
        self.manager.current = 'welcome'
