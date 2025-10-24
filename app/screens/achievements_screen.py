"""
Pantalla de Logros y Ranking
Muestra los logros desbloqueados y el ranking de usuarios
"""

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño de esta pantalla
Builder.load_file('app/screens/achievements_screen.kv')


class AchievementsScreen(MDScreen):
    """
    Pantalla que muestra los logros del usuario y el ranking global
    """
    
    def volver_home(self):
        """Navega de vuelta a la pantalla de inicio"""
        print("Volver a home desde logros")
        self.manager.current = 'home'

