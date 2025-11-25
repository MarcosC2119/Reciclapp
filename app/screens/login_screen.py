"""
Pantalla de inicio de sesión
Autor: Marcos Castro (mcastro2024@alu.uct.cl)
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/login_screen.kv')


class LoginScreen(MDScreen):
    """Pantalla de login para autenticación de usuarios"""
    
    def on_enter(self):
        """Llamado cuando se entra a la pantalla"""
        app = MDApp.get_running_app()
        app.analytics.track_screen_view('login')
    
    def toggle_password(self):
        """Alternar visibilidad de la contraseña"""
        password_input = self.ids.password_input
        password_input.password = not password_input.password
    
    def iniciar_sesion(self):
        """Procesar el inicio de sesión"""
        app = MDApp.get_running_app()
        
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        
        print(f"Iniciar sesión - Email: {email}")
        
        # Guardar datos de usuario en la base de datos
        app.db.update_user(email=email)
        
        # Track evento de login
        app.analytics.track_login('email')
        app.analytics.track_button_click('iniciar_sesion', 'login')
        
        # Navegar a home después de login
        self.manager.current = 'home'
    
    def continuar_google(self):
        """Iniciar sesión con Google"""
        app = MDApp.get_running_app()
        
        print("Continuar con Google")
        
        # Track evento de login
        app.analytics.track_login('google')
        app.analytics.track_button_click('continuar_google', 'login')
        
        # Por ahora navega a home
        self.manager.current = 'home'
    
    def ir_registro(self):
        """Navegar a la pantalla de registro"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ir_registro', 'login')
        
        print("Ir a registro")
        # Aquí puedes navegar a la pantalla de registro
        # self.manager.current = 'registro'
    
    def volver(self):
        """Volver a la pantalla de bienvenida"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('volver', 'login')
        
        print("Volver a welcome")
        self.manager.current = 'welcome'


