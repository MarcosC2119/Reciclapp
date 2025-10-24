"""
Tests unitarios para las pantallas de la aplicación
"""

import pytest
from unittest.mock import Mock, patch, MagicMock


class TestWelcomeScreen:
    """Tests para la pantalla de bienvenida"""
    
    @pytest.mark.unit
    def test_welcome_screen_exists(self):
        """Verifica que la clase WelcomeScreen existe"""
        from app.screens.welcome_screen import WelcomeScreen
        assert WelcomeScreen is not None
    
    @pytest.mark.unit
    def test_welcome_screen_comenzar_method(self):
        """Verifica que el método comenzar existe y funciona"""
        from app.screens.welcome_screen import WelcomeScreen
        screen = WelcomeScreen()
        screen.manager = Mock()
        
        # Ejecutar el método comenzar
        screen.comenzar()
        
        # Verificar que cambió a la pantalla de login
        assert screen.manager.current == 'login'


class TestLoginScreen:
    """Tests para la pantalla de login"""
    
    @pytest.mark.unit
    def test_login_screen_exists(self):
        """Verifica que la clase LoginScreen existe"""
        from app.screens.login_screen import LoginScreen
        assert LoginScreen is not None
    
    @pytest.mark.unit
    def test_toggle_password(self):
        """Verifica que el toggle de contraseña funciona"""
        from app.screens.login_screen import LoginScreen
        screen = LoginScreen()
        
        # Mock del input de contraseña
        mock_password_input = Mock()
        mock_password_input.password = True
        screen.ids = {'password_input': mock_password_input}
        
        # Toggle contraseña
        screen.toggle_password()
        
        # Verificar que cambió el estado
        assert mock_password_input.password == False
    
    @pytest.mark.unit
    def test_iniciar_sesion(self):
        """Verifica que el método iniciar_sesion funciona"""
        from app.screens.login_screen import LoginScreen
        screen = LoginScreen()
        
        # Mock de los inputs
        mock_email = Mock()
        mock_email.text = "test@example.com"
        mock_password = Mock()
        mock_password.text = "password123"
        
        screen.ids = {
            'email_input': mock_email,
            'password_input': mock_password
        }
        screen.manager = Mock()
        
        # Ejecutar inicio de sesión
        screen.iniciar_sesion()
        
        # Verificar que se intentó hacer login
        assert screen.manager.current == 'home'
    
    @pytest.mark.unit
    def test_volver_welcome(self):
        """Verifica que el botón volver navega a welcome"""
        from app.screens.login_screen import LoginScreen
        screen = LoginScreen()
        screen.manager = Mock()
        
        screen.volver()
        
        assert screen.manager.current == 'welcome'


class TestHomeScreen:
    """Tests para la pantalla principal/home"""
    
    @pytest.mark.unit
    def test_home_screen_exists(self):
        """Verifica que la clase HomeScreen existe"""
        from app.screens.home_screen import HomeScreen
        assert HomeScreen is not None
    
    @pytest.mark.unit
    def test_ir_comunidad(self):
        """Verifica navegación a comunidad"""
        from app.screens.home_screen import HomeScreen
        screen = HomeScreen()
        screen.manager = Mock()
        
        screen.ir_comunidad()
        
        assert screen.manager.current == 'community'
    
    @pytest.mark.unit
    def test_ir_logros(self):
        """Verifica que el método ir_logros existe"""
        from app.screens.home_screen import HomeScreen
        screen = HomeScreen()
        screen.manager = Mock()
        
        # El método existe pero la navegación está comentada por ahora
        screen.ir_logros()
        
        # Solo verificamos que el método no lance error
        assert hasattr(screen, 'ir_logros')
    
    @pytest.mark.unit
    def test_ir_perfil(self):
        """Verifica navegación a perfil"""
        from app.screens.home_screen import HomeScreen
        screen = HomeScreen()
        screen.manager = Mock()
        
        screen.ir_perfil()
        
        assert screen.manager.current == 'profile'


class TestCommunityScreen:
    """Tests para la pantalla de comunidad"""
    
    @pytest.mark.unit
    def test_community_screen_exists(self):
        """Verifica que la clase CommunityScreen existe"""
        from app.screens.community_screen import CommunityScreen
        assert CommunityScreen is not None
    
    @pytest.mark.unit
    def test_navegar_home(self):
        """Verifica navegación de vuelta a home"""
        from app.screens.community_screen import CommunityScreen
        screen = CommunityScreen()
        screen.manager = Mock()
        
        screen.navegar_home()
        
        assert screen.manager.current == 'home'
    
    @pytest.mark.unit
    def test_navegar_perfil(self):
        """Verifica navegación a perfil"""
        from app.screens.community_screen import CommunityScreen
        screen = CommunityScreen()
        screen.manager = Mock()
        
        screen.navegar_perfil()
        
        assert screen.manager.current == 'profile'


class TestAchievementsScreen:
    """Tests para la pantalla de logros"""
    
    @pytest.mark.unit
    def test_achievements_screen_exists(self):
        """Verifica que la clase AchievementsScreen existe"""
        from app.screens.achievements_screen import AchievementsScreen
        assert AchievementsScreen is not None


class TestProfileScreen:
    """Tests para la pantalla de perfil"""
    
    @pytest.mark.unit
    def test_profile_screen_exists(self):
        """Verifica que la clase ProfileScreen existe"""
        from app.screens.profile_screen import ProfileScreen
        assert ProfileScreen is not None
    
    @pytest.mark.unit
    def test_volver_home(self):
        """Verifica navegación de vuelta a home"""
        from app.screens.profile_screen import ProfileScreen
        screen = ProfileScreen()
        screen.manager = Mock()
        
        screen.volver_home()
        
        assert screen.manager.current == 'home'
    
    @pytest.mark.unit
    def test_cerrar_sesion(self):
        """Verifica que cerrar sesión navega a welcome"""
        from app.screens.profile_screen import ProfileScreen
        screen = ProfileScreen()
        screen.manager = Mock()
        
        screen.cerrar_sesion()
        
        assert screen.manager.current == 'welcome'

