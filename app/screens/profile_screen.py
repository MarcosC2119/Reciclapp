"""
Pantalla de perfil de usuario
Autor: Marcos Castro (mcastro2024@alu.uct.cl)
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/profile_screen.kv')


class ProfileScreen(MDScreen):
    """
    Pantalla de perfil del usuario
    
    Muestra información del usuario y configuración
    """
    
    def on_enter(self):
        """Llamado cuando se entra a la pantalla"""
        app = MDApp.get_running_app()
        app.analytics.track_screen_view('profile')
        
        # Obtener y mostrar datos del usuario
        user = app.db.get_user()
        print(f"📱 Perfil: {user['name']} ({user['email']})")
    
    def editar_perfil(self):
        """Permite editar el perfil del usuario"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('editar_perfil', 'profile')
        print("Editando perfil")
    
    def volver_home(self):
        """Navega de vuelta a la pantalla de inicio"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('volver_home', 'profile')
        print("Volver a home desde perfil")
        self.manager.current = 'home'
    
    def cerrar_sesion(self):
        """Cierra la sesión del usuario"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('cerrar_sesion', 'profile')
        print("Cerrando sesión...")
        self.manager.current = 'welcome'
