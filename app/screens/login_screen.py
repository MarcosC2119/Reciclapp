"""
Pantalla de inicio de sesión
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/login_screen.kv')


class LoginScreen(MDScreen):
    """Pantalla de login para autenticación de usuarios"""
    
    def toggle_password(self):
        """Alternar visibilidad de la contraseña"""
        password_input = self.ids.password_input
        password_input.password = not password_input.password
    
    def iniciar_sesion(self):
        """Procesar el inicio de sesión"""
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        print(f"Iniciar sesión - Email: {email}")
        # Aquí puedes agregar la lógica de autenticación
        # Por ahora navega a home después de login
        self.manager.current = 'home'
    
    def continuar_google(self):
        """Iniciar sesión con Google"""
        print("Continuar con Google")
        # Aquí puedes agregar la lógica de Google Sign-In
        # Por ahora navega a home
        self.manager.current = 'home'
    
    def ir_registro(self):
        """Navegar a la pantalla de registro"""
        print("Ir a registro")
        # Aquí puedes navegar a la pantalla de registro
        # self.manager.current = 'registro'
    
    def volver(self):
        """Volver a la pantalla de bienvenida"""
        print("Volver a welcome")
        self.manager.current = 'welcome'

