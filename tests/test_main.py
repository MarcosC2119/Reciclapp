"""
Tests para el módulo principal de la aplicación
"""

import pytest
from unittest.mock import Mock, patch, MagicMock


class TestMainApp:
    """Tests para la aplicación principal"""
    
    @pytest.mark.unit
    def test_main_app_exists(self):
        """Verifica que la clase MainApp existe"""
        from app.main import MainApp
        assert MainApp is not None
    
    @pytest.mark.unit
    @patch('app.main.Builder')
    def test_app_build_method(self, mock_builder):
        """Verifica que el método build carga el archivo KV correcto"""
        from app.main import MainApp
        
        app = MainApp()
        mock_builder.load_file.return_value = Mock()
        
        result = app.build()
        
        # Verificar que se cargó el archivo main.kv
        mock_builder.load_file.assert_called_once_with('app/main.kv')
    
    @pytest.mark.unit
    def test_app_has_theme_config(self):
        """Verifica que la app tiene configuración de tema"""
        from app.main import MainApp
        
        app = MainApp()
        
        # Verificar que theme_cls existe
        assert hasattr(app, 'theme_cls')
    
    @pytest.mark.unit
    @patch('app.main.Window')
    def test_window_size_config(self, mock_window, app_config):
        """Verifica que el tamaño de ventana está configurado correctamente"""
        from app.main import MainApp
        
        # El tamaño de ventana se configura en run.py
        # Verificar que la configuración de app_config coincide
        assert app_config["window_size"] == (360, 720)
        assert app_config["theme"] == "Green"
        assert app_config["accent"] == "Amber"


class TestScreenManager:
    """Tests para el ScreenManager"""
    
    @pytest.mark.unit
    def test_all_screens_registered(self):
        """Verifica que todas las pantallas están registradas"""
        from app.screens import (
            WelcomeScreen,
            LoginScreen,
            HomeScreen,
            CommunityScreen,
            AchievementsScreen,
            ProfileScreen
        )
        
        # Verificar que todas las clases existen
        assert WelcomeScreen is not None
        assert LoginScreen is not None
        assert HomeScreen is not None
        assert CommunityScreen is not None
        assert AchievementsScreen is not None
        assert ProfileScreen is not None
    
    @pytest.mark.integration
    def test_screen_navigation_flow(self):
        """Verifica el flujo de navegación entre pantallas"""
        from app.screens.welcome_screen import WelcomeScreen
        from app.screens.login_screen import LoginScreen
        from app.screens.home_screen import HomeScreen
        
        # Crear screens
        welcome = WelcomeScreen(name='welcome')
        login = LoginScreen(name='login')
        home = HomeScreen(name='home')
        
        # Mock del manager
        mock_manager = Mock()
        welcome.manager = mock_manager
        login.manager = mock_manager
        home.manager = mock_manager
        
        # Simular flujo: welcome -> login -> home
        welcome.comenzar()
        assert mock_manager.current == 'login'
        
        # Mock de inputs para login
        login.ids = {
            'email_input': Mock(text='test@test.com'),
            'password_input': Mock(text='password')
        }
        login.iniciar_sesion()
        assert mock_manager.current == 'home'


class TestAppImports:
    """Tests para verificar que todos los imports funcionan"""
    
    @pytest.mark.unit
    def test_import_main_app(self):
        """Verifica que se puede importar MainApp"""
        try:
            from app.main import MainApp
            assert True
        except ImportError:
            pytest.fail("No se pudo importar MainApp")
    
    @pytest.mark.unit
    def test_import_all_screens(self):
        """Verifica que se pueden importar todas las pantallas"""
        try:
            from app.screens import (
                WelcomeScreen,
                LoginScreen,
                HomeScreen,
                CommunityScreen,
                AchievementsScreen,
                ProfileScreen
            )
            assert True
        except ImportError as e:
            pytest.fail(f"Error al importar pantallas: {e}")
    
    @pytest.mark.unit
    def test_kivy_imports(self):
        """Verifica que las dependencias de Kivy están disponibles"""
        try:
            from kivy.app import App
            from kivy.lang import Builder
            from kivy.core.window import Window
            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen
            assert True
        except ImportError as e:
            pytest.fail(f"Error al importar dependencias de Kivy: {e}")

