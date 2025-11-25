"""
Pantalla de EcoPuntos - Reciclapp
Permite ver y guardar puntos de reciclaje cercanos.
"""
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/ecopuntos_screen.kv')


class EcoPuntosScreen(MDScreen):
    """
    Pantalla que muestra mapa (simulado) y lista de EcoPuntos.
    Permite guardar nuevos puntos.
    """
    dialog = None
    
    def on_enter(self):
        """Al entrar, cargar los puntos guardados"""
        self.load_saved_locations()
        
    def load_saved_locations(self):
        """Carga las ubicaciones desde la base de datos"""
        app = MDApp.get_running_app()
        locations = app.db.get_saved_locations()
        
        # Limpiar lista actual (excepto el header si lo hubiera)
        self.ids.locations_list.clear_widgets()
        
        # Agregar widgets para cada ubicación
        from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget
        
        for loc in locations:
            item = TwoLineAvatarIconListItem(
                text=loc['name'],
                secondary_text=loc['address']
            )
            icon = IconLeftWidget(icon="map-marker")
            item.add_widget(icon)
            self.ids.locations_list.add_widget(item)
            
    def show_add_dialog(self):
        """Muestra diálogo para agregar nuevo punto"""
        if not self.dialog:
            self.name_field = MDTextField(
                hint_text="Nombre del lugar",
                helper_text="Ej: Punto Limpio Central",
                helper_text_mode="on_focus"
            )
            self.address_field = MDTextField(
                hint_text="Dirección",
                helper_text="Ej: Av. Principal 123",
                helper_text_mode="on_focus"
            )
            
            content = MDBoxLayout(
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="120dp"
            )
            content.add_widget(self.name_field)
            content.add_widget(self.address_field)
            
            self.dialog = MDDialog(
                title="Nuevo EcoPunto",
                type="custom",
                content_cls=content,
                buttons=[
                    MDFlatButton(
                        text="CANCELAR",
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="GUARDAR",
                        on_release=self.save_location
                    ),
                ],
            )
        self.dialog.open()
        
    def close_dialog(self, *args):
        """Cierra el diálogo"""
        if self.dialog:
            self.dialog.dismiss()
            
    def save_location(self, *args):
        """Guarda la ubicación en la BD"""
        name = self.name_field.text
        address = self.address_field.text
        
        if name and address:
            app = MDApp.get_running_app()
            app.db.add_saved_location(name, address, "custom")
            
            # Limpiar campos
            self.name_field.text = ""
            self.address_field.text = ""
            
            self.close_dialog()
            self.load_saved_locations()
            
    def volver_home(self):
        """Vuelve al inicio"""
        self.manager.current = 'home'
