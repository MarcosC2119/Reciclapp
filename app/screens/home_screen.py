"""
Pantalla de inicio (Dashboard) - Página principal después del login
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/home_screen.kv')


class HomeScreen(MDScreen):
    """
    Pantalla principal de la aplicación con dashboard completo
    
    Muestra:
    - Saludo y estadísticas (EcoTokens, Racha)
    - Progreso semanal
    - Acciones rápidas
    - Actividad reciente
    - Comunidad e Impacto
    - Navegación inferior
    """
    
    def on_enter(self):
        """Llamado cuando se entra a la pantalla"""
        # Aquí puedes cargar datos del usuario, actualizar estadísticas, etc.
        pass
    
    def escanear_qr(self):
        """Abrir escáner QR"""
        print("Abriendo escáner QR")
        # self.manager.current = 'qr_scanner'
    
    def ir_ecopuntos(self):
        """Navegar a EcoPuntos"""
        print("Navegando a EcoPuntos")
        # self.manager.current = 'map'
    
    def ir_recompensas(self):
        """Navegar a Recompensas"""
        print("Navegando a Recompensas")
        # self.manager.current = 'rewards'
    
    def ir_logros(self):
        """Navegar a Logros"""
        print("Navegando a Logros")
        # self.manager.current = 'achievements'
    
    def ir_comunidad(self):
        """Navegar a Comunidad"""
        print("Navegando a Comunidad")
        # self.manager.current = 'community'
    
    def ir_perfil(self):
        """Navegar a Perfil"""
        print("Navegando a Perfil")
        self.manager.current = 'profile'
    
    def ver_impacto(self):
        """Ver detalles del impacto ambiental"""
        print("Viendo impacto ambiental")
        # self.manager.current = 'impact'
