"""
Pantalla de inicio de sesión
Implementa autenticación de usuarios con KivyMD
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp

class LoginScreen(MDScreen):
    """Pantalla de inicio de sesión"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        """Construir la interfaz de usuario"""
        # Layout principal
        main_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(20),
            adaptive_height=True
        )
        
        # Toolbar superior
        toolbar = MDTopAppBar(
            title="Reciclapp",
            elevation=2,
            md_bg_color=self.theme_cls.primary_color
        )
        main_layout.add_widget(toolbar)
        
        # Card de login
        login_card = MDCard(
            size_hint=(None, None),
            size=(dp(300), dp(400)),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            elevation=4,
            radius=[15, 15, 15, 15]
        )
        
        # Layout del card
        card_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(20)
        )
        
        # Título
        title = MDLabel(
            text="Iniciar Sesión",
            theme_text_color="Primary",
            size_hint_y=None,
            height=dp(40),
            halign="center",
            font_style="H4"
        )
        card_layout.add_widget(title)
        
        # Campo de email
        self.email_field = MDTextField(
            hint_text="Correo electrónico",
            helper_text="Ingresa tu email",
            helper_text_mode="on_focus",
            size_hint_y=None,
            height=dp(60),
            icon_right="email"
        )
        card_layout.add_widget(self.email_field)
        
        # Campo de contraseña
        self.password_field = MDTextField(
            hint_text="Contraseña",
            helper_text="Ingresa tu contraseña",
            helper_text_mode="on_focus",
            password=True,
            size_hint_y=None,
            height=dp(60),
            icon_right="eye-off"
        )
        card_layout.add_widget(self.password_field)
        
        # Botón de login
        login_button = MDRaisedButton(
            text="Iniciar Sesión",
            size_hint_y=None,
            height=dp(50),
            md_bg_color=self.theme_cls.primary_color,
            on_release=self.login_user
        )
        card_layout.add_widget(login_button)
        
        # Botón de registro
        register_button = MDRaisedButton(
            text="Crear Cuenta",
            size_hint_y=None,
            height=dp(50),
            md_bg_color=self.theme_cls.accent_color,
            on_release=self.go_to_register
        )
        card_layout.add_widget(register_button)
        
        login_card.add_widget(card_layout)
        main_layout.add_widget(login_card)
        
        self.add_widget(main_layout)
    
    def login_user(self, instance):
        """Manejar el inicio de sesión"""
        email = self.email_field.text
        password = self.password_field.text
        
        if email and password:
            # Aquí iría la lógica de autenticación
            print(f"Login intentado: {email}")
            # Cambiar a pantalla principal
            self.manager.current = 'home'
        else:
            # Mostrar error
            print("Por favor completa todos los campos")
    
    def go_to_register(self, instance):
        """Ir a pantalla de registro"""
        print("Ir a registro")
        # Aquí cambiarías a la pantalla de registro
