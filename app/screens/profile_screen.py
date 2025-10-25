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
        # Mostrar mensaje de confirmación
        self.show_logout_dialog()
    
    def show_logout_dialog(self):
        """Muestra diálogo de confirmación de cierre de sesión"""
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton
        
        self.dialog = MDDialog(
            title="Cerrar Sesión",
            text="¿Estás seguro de que quieres cerrar sesión?",
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="Cerrar Sesión",
                    on_release=lambda x: self.confirm_logout()
                )
            ]
        )
        self.dialog.open()
    
    def confirm_logout(self):
        """Confirma el cierre de sesión"""
        if self.dialog:
            self.dialog.dismiss()
        
        # Limpiar usuario actual si existe
        if hasattr(self.manager, 'app') and hasattr(self.manager.app, 'current_user'):
            self.manager.app.current_user = None
        
        # Mostrar mensaje de despedida
        self.show_goodbye_dialog()
    
    def show_goodbye_dialog(self):
        """Muestra mensaje de despedida"""
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton
        
        self.dialog = MDDialog(
            title="¡Hasta pronto!",
            text="Has cerrado sesión correctamente. ¡Gracias por usar Reciclapp!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.go_to_welcome()
                )
            ]
        )
        self.dialog.open()
    
    def go_to_welcome(self):
        """Navegar a la pantalla de bienvenida"""
        if self.dialog:
            self.dialog.dismiss()
        self.manager.current = 'welcome'
