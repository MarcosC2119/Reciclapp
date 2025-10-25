"""
Modelo de Usuario para Reciclapp
"""
import sqlite3
from datetime import datetime
from typing import Optional, Dict, Any


class User:
    """Modelo de usuario para la aplicación de reciclaje"""
    
    def __init__(self, user_id: int = None, username: str = "", email: str = "", 
                 password: str = "", name: str = "", ecotokens: int = 0, 
                 streak: int = 0, recycled_items: int = 0, co2_saved: float = 0.0,
                 level: int = 1, rank: str = "Eco Novice", created_at: str = None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.ecotokens = ecotokens
        self.streak = streak
        self.recycled_items = recycled_items
        self.co2_saved = co2_saved
        self.level = level
        self.rank = rank
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el usuario a diccionario"""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'ecotokens': self.ecotokens,
            'streak': self.streak,
            'recycled_items': self.recycled_items,
            'co2_saved': self.co2_saved,
            'level': self.level,
            'rank': self.rank,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Crea un usuario desde un diccionario"""
        return cls(
            user_id=data.get('user_id'),
            username=data.get('username', ''),
            email=data.get('email', ''),
            password=data.get('password', ''),
            name=data.get('name', ''),
            ecotokens=data.get('ecotokens', 0),
            streak=data.get('streak', 0),
            recycled_items=data.get('recycled_items', 0),
            co2_saved=data.get('co2_saved', 0.0),
            level=data.get('level', 1),
            rank=data.get('rank', 'Eco Novice'),
            created_at=data.get('created_at')
        )
