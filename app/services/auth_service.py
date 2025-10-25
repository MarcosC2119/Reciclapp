"""
Servicio de autenticación para Reciclapp
"""
from typing import Optional
from app.database.database import Database
from app.models.user import User


class AuthService:
    """Servicio para manejar autenticación de usuarios"""
    
    def __init__(self):
        self.db = Database()
    
    def login(self, username_or_email: str, password: str) -> Optional[User]:
        """
        Autentica un usuario
        
        Args:
            username_or_email: Username o email del usuario
            password: Contraseña del usuario
            
        Returns:
            User si la autenticación es exitosa, None en caso contrario
        """
        return self.db.authenticate_user(username_or_email, password)
    
    def register(self, username: str, email: str, password: str, name: str) -> Optional[User]:
        """
        Registra un nuevo usuario
        
        Args:
            username: Nombre de usuario único
            email: Email único
            password: Contraseña
            name: Nombre completo
            
        Returns:
            User si el registro es exitoso, None si ya existe
        """
        user = User(
            username=username,
            email=email,
            password=password,
            name=name,
            ecotokens=100,  # EcoTokens iniciales
            streak=0,
            recycled_items=0,
            co2_saved=0.0,
            level=1,
            rank="Eco Novice"
        )
        
        return self.db.create_user(user)
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Obtiene un usuario por username"""
        return self.db.get_user_by_username(username)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Obtiene un usuario por email"""
        return self.db.get_user_by_email(email)
    
    def update_user(self, user: User) -> bool:
        """Actualiza un usuario"""
        return self.db.update_user(user)
