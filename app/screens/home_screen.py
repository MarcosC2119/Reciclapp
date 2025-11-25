"""
Pantalla de inicio (Dashboard) - Página principal después del login
Autor: Marcos Castro (mcastro2024@alu.uct.cl)
"""
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
import random

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/home_screen.kv')


class HomeScreen(MDScreen):
    """
    Pantalla principal de la aplicación con dashboard completo
    
    Muestra:
    - Saludo y estadísticas (EcoTokens, Racha)
    - Progreso semanal
    - Acciones rápidas
    - Actividad reciente
    - Comunidad e Impacto
    - Navegación inferior
    """
    
    def on_enter(self):
        """Llamado cuando se entra a la pantalla"""
        app = MDApp.get_running_app()
        app.analytics.track_screen_view('home')
        
        # Aquí puedes actualizar los widgets con datos reales
        # Por ejemplo, actualizar labels con eco-tokens, racha, etc.
        self.update_dashboard_data()
    
    def update_dashboard_data(self):
        """Actualiza los datos del dashboard desde la base de datos"""
        app = MDApp.get_running_app()
        
        # Obtener datos del usuario
        user = app.db.get_user()
        eco_tokens = app.db.get_eco_tokens()
        streak = app.db.get_streak()
        
        print(f"[STATS] Dashboard actualizado - Tokens: {eco_tokens}, Racha: {streak}")
        
        # Aquí podrías actualizar los widgets de la UI si tienes IDs asignados
        # Por ejemplo: self.ids.eco_tokens_label.text = str(eco_tokens)
    
    def escanear_qr(self):
        """Simula escaneo de QR y registro de reciclaje"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('escanear_qr', 'home')
        
        # Simular reciclaje de un material aleatorio
        materials = ['plastic', 'paper', 'glass', 'metal', 'organic']
        material = random.choice(materials)
        quantity = random.randint(1, 5)
        eco_tokens = quantity * 10
        
        # Registrar en la base de datos
        app.db.add_recycling_item(material, quantity, eco_tokens)
        app.analytics.track_recycling_action(material, quantity, eco_tokens)
        
        # Incrementar racha
        app.db.increment_streak()
        
        print(f"[OK] QR escaneado: {quantity}x {material}")
        print(f"[COINS] Ganaste {eco_tokens} eco-tokens!")
        
        # Actualizar dashboard
        self.update_dashboard_data()
        
        # Verificar logros
        self.check_achievements()
    
    def ir_ecopuntos(self):
        """Navegar a EcoPuntos"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ir_ecopuntos', 'home')
        print("Navegando a EcoPuntos")
        self.manager.current = 'ecopuntos'
    
    def ir_recompensas(self):
        """Navegar a Recompensas"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ir_recompensas', 'home')
        print("Navegando a Recompensas")
        self.manager.current = 'rewards'
    
    def ir_logros(self):
        """Navegar a Logros"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ir_logros', 'home')
        print("Navegando a Logros")
        self.manager.current = 'achievements'
    
    def ir_comunidad(self):
        """Navegar a Comunidad"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ir_comunidad', 'home')
        print("Navegando a Comunidad")
        self.manager.current = 'community'
    
    def ir_perfil(self):
        """Navegar a Perfil"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ir_perfil', 'home')
        print("Navegando a Perfil")
        self.manager.current = 'profile'
    
    def ver_impacto(self):
        """Ver detalles del impacto ambiental"""
        app = MDApp.get_running_app()
        app.analytics.track_button_click('ver_impacto', 'home')
        
        # Obtener datos de impacto
        impact = app.db.get_environmental_impact()
        print(f"[IMPACT] Impacto ambiental:")
        print(f"  CO2 ahorrado: {impact['co2_saved']:.2f} kg")
        print(f"  Agua ahorrada: {impact['water_saved']:.2f} litros")
    
    def check_achievements(self):
        """Verifica y desbloquea logros basados en el progreso"""
        app = MDApp.get_running_app()
        
        eco_tokens = app.db.get_eco_tokens()
        total_recycled = app.db.get_total_items_recycled()
        streak = app.db.get_streak()
        
        # Logro: Primer reciclaje
        if total_recycled >= 1:
            unlocked = app.db.unlock_achievement(
                'first_recycle',
                'Primer Paso',
                'Reciclaste tu primer item'
            )
            if unlocked:
                app.analytics.track_achievement_unlocked('first_recycle', 'Primer Paso')
        
        # Logro: 10 items reciclados
        if total_recycled >= 10:
            unlocked = app.db.unlock_achievement(
                'eco_warrior_10',
                'Eco Guerrero',
                'Reciclaste 10 items'
            )
            if unlocked:
                app.analytics.track_achievement_unlocked('eco_warrior_10', 'Eco Guerrero')
        
        # Logro: 100 eco-tokens
        if eco_tokens >= 100:
            unlocked = app.db.unlock_achievement(
                'token_collector',
                'Coleccionista',
                'Acumulaste 100 eco-tokens'
            )
            if unlocked:
                app.analytics.track_achievement_unlocked('token_collector', 'Coleccionista')
        
        # Logro: Racha de 7 días
        if streak >= 7:
            unlocked = app.db.unlock_achievement(
                'week_streak',
                'Semana Completa',
                'Mantuviste una racha de 7 días'
            )
            if unlocked:
                app.analytics.track_achievement_unlocked('week_streak', 'Semana Completa')

