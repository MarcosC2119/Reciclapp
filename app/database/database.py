"""
Configuración y conexión a la base de datos SQLite
"""
import sqlite3
import os
from typing import Optional, List, Dict, Any
from app.models.user import User


class Database:
    """Manejador de base de datos SQLite para Reciclapp"""
    
    def __init__(self, db_path: str = "reciclapp.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self) -> sqlite3.Connection:
        """Obtiene una conexión a la base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para acceder a columnas por nombre
        return conn
    
    def init_database(self):
        """Inicializa la base de datos y crea las tablas necesarias"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Crear tabla de usuarios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL,
                    ecotokens INTEGER DEFAULT 0,
                    streak INTEGER DEFAULT 0,
                    recycled_items INTEGER DEFAULT 0,
                    co2_saved REAL DEFAULT 0.0,
                    level INTEGER DEFAULT 1,
                    rank TEXT DEFAULT 'Eco Novice',
                    created_at TEXT NOT NULL
                )
            ''')
            
            conn.commit()
    
    def create_user(self, user: User) -> Optional[User]:
        """Crea un nuevo usuario en la base de datos"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, email, password, name, ecotokens, 
                                     streak, recycled_items, co2_saved, level, rank, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (user.username, user.email, user.password, user.name, 
                      user.ecotokens, user.streak, user.recycled_items, 
                      user.co2_saved, user.level, user.rank, user.created_at))
                
                user_id = cursor.lastrowid
                conn.commit()
                
                # Retornar el usuario creado con el ID asignado
                return self.get_user_by_id(user_id)
        except sqlite3.IntegrityError:
            return None  # Usuario ya existe
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Obtiene un usuario por su nombre de usuario"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            row = cursor.fetchone()
            
            if row:
                return User.from_dict(dict(row))
            return None
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Obtiene un usuario por su email"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            row = cursor.fetchone()
            
            if row:
                return User.from_dict(dict(row))
            return None
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Obtiene un usuario por su ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            row = cursor.fetchone()
            
            if row:
                return User.from_dict(dict(row))
            return None
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Autentica un usuario con username/email y contraseña"""
        # Buscar por username primero
        user = self.get_user_by_username(username)
        
        # Si no se encuentra, buscar por email
        if not user:
            user = self.get_user_by_email(username)
        
        # Verificar contraseña
        if user and user.password == password:
            return user
        
        return None
    
    def update_user(self, user: User) -> bool:
        """Actualiza un usuario en la base de datos"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users SET 
                        username = ?, email = ?, password = ?, name = ?,
                        ecotokens = ?, streak = ?, recycled_items = ?, 
                        co2_saved = ?, level = ?, rank = ?
                    WHERE user_id = ?
                ''', (user.username, user.email, user.password, user.name,
                      user.ecotokens, user.streak, user.recycled_items,
                      user.co2_saved, user.level, user.rank, user.user_id))
                
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
    
    def get_all_users(self) -> List[User]:
        """Obtiene todos los usuarios"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
            rows = cursor.fetchall()
            
            return [User.from_dict(dict(row)) for row in rows]
