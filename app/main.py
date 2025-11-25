"""
Aplicación principal KivyMD - Reciclapp
Autor: Marcos Castro (mcastro2024@alu.uct.cl)
"""
import sys
import os

# Agregar el directorio raíz al path si no está
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Configurar tamaño de ventana (aspecto smartphone 18:9)
from kivy.core.window import Window
Window.size = (360, 720)  # Smartphone moderno (18:9 aspect ratio - 2:1)

from kivymd.app import MDApp
from kivy.lang import Builder
from app.screens.welcome_screen import WelcomeScreen
from app.screens.login_screen import LoginScreen
from app.screens.home_screen import HomeScreen
from app.screens.profile_screen import ProfileScreen
from app.screens.community_screen import CommunityScreen
from app.screens.community_screen import CommunityScreen
from app.screens.achievements_screen import AchievementsScreen
from app.screens.ecopuntos_screen import EcoPuntosScreen
from app.screens.rewards_screen import RewardsScreen

# Importar sistemas de persistencia y métricas
from app.database import Database
from app.analytics import Analytics


class MainApp(MDApp):
    """Aplicación principal - Reciclapp"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Inicializar sistemas
        self.db = Database()
        self.analytics = Analytics()
    
    def build(self):
        """Construye la aplicación"""
        # Configuración del tema
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        
        # Cargar el archivo KV principal
        sm = Builder.load_file('app/main.kv')
        
        # Establecer la pantalla de bienvenida como inicial
        sm.current = 'welcome'
        
        # Iniciar sesión de analytics
        self.analytics.start_session()
        self.analytics.track_event('app_start')
        
        # Actualizar último login
        self.db.update_last_login()
        
        print(f"\n[OK] Reciclapp iniciada")
        print(f"[USER] Usuario: {self.db.get_user()['name']}")
        print(f"[COINS] Eco-tokens: {self.db.get_eco_tokens()}")
        print(f"[STREAK] Racha: {self.db.get_streak()} días\n")
        
        return sm
    
    def switch_screen(self, screen_name):
        """Cambia entre pantallas"""
        self.root.current = screen_name
        # Track la navegación
        self.analytics.track_screen_view(screen_name)
    
    def on_stop(self):
        """Llamado cuando la app se cierra"""
        # Finalizar sesión de analytics
        self.analytics.end_session()
        
        # Mostrar reporte de métricas
        print("\n" + "="*50)
        print("[STATS] Resumen de la sesión:")
        duration = self.analytics.get_session_duration()
        if duration:
            print(f"[TIME] Duración: {duration:.2f}s ({duration/60:.2f} min)")
        print(f"[COINS] Eco-tokens finales: {self.db.get_eco_tokens()}")
        print(f"[RECYCLED] Items reciclados: {self.db.get_total_items_recycled()}")
        print("="*50 + "\n")
        
        return super().on_stop()


if __name__ == '__main__':
    MainApp().run()

