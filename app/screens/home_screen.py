"""
Pantalla principal de la aplicación
Muestra el dashboard principal después del login
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp

class HomeScreen(MDScreen):
    """Pantalla principal de la aplicación"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        """Construir la interfaz de usuario"""
        # Layout principal
        main_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10)
        )
        
        # Toolbar superior
        toolbar = MDTopAppBar(
            title="Reciclapp",
            elevation=2,
            md_bg_color=self.theme_cls.primary_color,
            right_action_items=[["logout", self.logout_user]]
        )
        main_layout.add_widget(toolbar)
        
        # Saludo
        welcome_label = MDLabel(
            text="¡Bienvenido a Reciclapp!",
            theme_text_color="Primary",
            size_hint_y=None,
            height=dp(40),
            halign="center",
            font_style="H5"
        )
        main_layout.add_widget(welcome_label)
        
        # Grid de opciones principales
        options_grid = MDGridLayout(
            cols=2,
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        
        # Card de reciclaje
        recycle_card = MDCard(
            elevation=4,
            radius=[15, 15, 15, 15],
            on_release=self.go_to_recycling
        )
        
        recycle_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(10)
        )
        
        recycle_icon = MDIconButton(
            icon="recycle",
            theme_icon_color="Primary",
            size_hint_y=None,
            height=dp(60)
        )
        recycle_layout.add_widget(recycle_icon)
        
        recycle_label = MDLabel(
            text="Reciclar",
            theme_text_color="Primary",
            halign="center",
            font_style="H6"
        )
        recycle_layout.add_widget(recycle_label)
        
        recycle_card.add_widget(recycle_layout)
        options_grid.add_widget(recycle_card)
        
        # Card de estadísticas
        stats_card = MDCard(
            elevation=4,
            radius=[15, 15, 15, 15],
            on_release=self.go_to_stats
        )
        
        stats_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(10)
        )
        
        stats_icon = MDIconButton(
            icon="chart-line",
            theme_icon_color="Primary",
            size_hint_y=None,
            height=dp(60)
        )
        stats_layout.add_widget(stats_icon)
        
        stats_label = MDLabel(
            text="Estadísticas",
            theme_text_color="Primary",
            halign="center",
            font_style="H6"
        )
        stats_layout.add_widget(stats_label)
        
        stats_card.add_widget(stats_layout)
        options_grid.add_widget(stats_card)
        
        # Card de perfil
        profile_card = MDCard(
            elevation=4,
            radius=[15, 15, 15, 15],
            on_release=self.go_to_profile
        )
        
        profile_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(10)
        )
        
        profile_icon = MDIconButton(
            icon="account",
            theme_icon_color="Primary",
            size_hint_y=None,
            height=dp(60)
        )
        profile_layout.add_widget(profile_icon)
        
        profile_label = MDLabel(
            text="Perfil",
            theme_text_color="Primary",
            halign="center",
            font_style="H6"
        )
        profile_layout.add_widget(profile_label)
        
        profile_card.add_widget(profile_layout)
        options_grid.add_widget(profile_card)
        
        # Card de ayuda
        help_card = MDCard(
            elevation=4,
            radius=[15, 15, 15, 15],
            on_release=self.go_to_help
        )
        
        help_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(10)
        )
        
        help_icon = MDIconButton(
            icon="help-circle",
            theme_icon_color="Primary",
            size_hint_y=None,
            height=dp(60)
        )
        help_layout.add_widget(help_icon)
        
        help_label = MDLabel(
            text="Ayuda",
            theme_text_color="Primary",
            halign="center",
            font_style="H6"
        )
        help_layout.add_widget(help_label)
        
        help_card.add_widget(help_layout)
        options_grid.add_widget(help_card)
        
        main_layout.add_widget(options_grid)
        self.add_widget(main_layout)
    
    def logout_user(self, instance):
        """Cerrar sesión del usuario"""
        print("Cerrando sesión...")
        self.manager.current = 'login'
    
    def go_to_recycling(self, instance):
        """Ir a pantalla de reciclaje"""
        print("Ir a reciclaje")
    
    def go_to_stats(self, instance):
        """Ir a pantalla de estadísticas"""
        print("Ir a estadísticas")
    
    def go_to_profile(self, instance):
        """Ir a pantalla de perfil"""
        print("Ir a perfil")
    
    def go_to_help(self, instance):
        """Ir a pantalla de ayuda"""
        print("Ir a ayuda")
