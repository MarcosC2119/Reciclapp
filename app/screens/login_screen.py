"""
Pantalla de inicio de sesión
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from app.services.auth_service import AuthService

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/login_screen.kv')


class LoginScreen(MDScreen):
    """Pantalla de login para autenticación de usuarios"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth_service = AuthService()
        self.dialog = None
    
    def toggle_password(self):
        """Alternar visibilidad de la contraseña"""
        password_input = self.ids.password_input
        password_input.password = not password_input.password
    
    def iniciar_sesion(self):
        """Procesar el inicio de sesión"""
        email = self.ids.email_input.text.strip()
        password = self.ids.password_input.text.strip()
        
        # Validar campos vacíos
        if not email or not password:
            self.show_error_dialog("Error", "Por favor completa todos los campos")
            return
        
        # Intentar autenticar
        user = self.auth_service.login(email, password)
        
        if user:
            print(f"Login exitoso: {user.name} ({user.username})")
            # Guardar usuario actual en la app (opcional)
            if hasattr(self.manager, 'app'):
                self.manager.app.current_user = user
            self.manager.current = 'home'
        else:
            self.show_error_dialog("Error de Login", "Usuario o contraseña incorrectos")
    
    def show_error_dialog(self, title: str, message: str):
        """Muestra un diálogo de error"""
        if self.dialog:
            self.dialog.dismiss()
        
        self.dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()
    
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

