"""
Pantalla de registro de nuevos usuarios
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from app.services.auth_service import AuthService

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/register_screen.kv')


class RegisterScreen(MDScreen):
    """Pantalla de registro para nuevos usuarios"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth_service = AuthService()
        self.dialog = None
    
    def toggle_password(self):
        """Alternar visibilidad de la contraseña"""
        password_input = self.ids.password_input
        password_input.password = not password_input.password
    
    def toggle_confirm_password(self):
        """Alternar visibilidad de la confirmación de contraseña"""
        confirm_password_input = self.ids.confirm_password_input
        confirm_password_input.password = not confirm_password_input.password
    
    def registrar_usuario(self):
        """Procesar el registro de nuevo usuario"""
        # Obtener datos del formulario
        username = self.ids.username_input.text.strip()
        email = self.ids.email_input.text.strip()
        name = self.ids.name_input.text.strip()
        password = self.ids.password_input.text.strip()
        confirm_password = self.ids.confirm_password_input.text.strip()
        
        # Validar campos vacíos
        if not all([username, email, name, password, confirm_password]):
            self.show_error_dialog("Error", "Por favor completa todos los campos")
            return
        
        # Validar email básico
        if "@" not in email or "." not in email:
            self.show_error_dialog("Error", "Por favor ingresa un email válido")
            return
        
        # Validar contraseñas coinciden
        if password != confirm_password:
            self.show_error_dialog("Error", "Las contraseñas no coinciden")
            return
        
        # Validar longitud de contraseña
        if len(password) < 6:
            self.show_error_dialog("Error", "La contraseña debe tener al menos 6 caracteres")
            return
        
        # Validar username único
        if len(username) < 3:
            self.show_error_dialog("Error", "El nombre de usuario debe tener al menos 3 caracteres")
            return
        
        # Intentar registrar usuario
        user = self.auth_service.register(username, email, password, name)
        
        if user:
            self.show_success_dialog(
                "¡Cuenta Creada!", 
                f"¡Felicidades {user.name}! Tu cuenta ha sido creada exitosamente. Ya puedes iniciar sesión."
            )
            # Limpiar formulario
            self.clear_form()
        else:
            self.show_error_dialog("Error de Registro", "El usuario o email ya existe. Intenta con otros datos.")
    
    def clear_form(self):
        """Limpiar todos los campos del formulario"""
        self.ids.username_input.text = ""
        self.ids.email_input.text = ""
        self.ids.name_input.text = ""
        self.ids.password_input.text = ""
        self.ids.confirm_password_input.text = ""
    
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
    
    def show_success_dialog(self, title: str, message: str):
        """Muestra un diálogo de éxito"""
        if self.dialog:
            self.dialog.dismiss()
        
        self.dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(
                    text="Iniciar Sesión",
                    on_release=lambda x: self.go_to_login()
                )
            ]
        )
        self.dialog.open()
    
    def go_to_login(self):
        """Navegar a la pantalla de login"""
        if self.dialog:
            self.dialog.dismiss()
        self.manager.current = 'login'
    
    def volver_login(self):
        """Volver a la pantalla de login"""
        print("Volver a login desde registro")
        self.manager.current = 'login'
