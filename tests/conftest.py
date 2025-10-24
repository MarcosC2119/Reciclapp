"""
Configuración compartida de pytest para todos los tests
Define fixtures y configuraciones globales
"""

import pytest
import os
import sys

# Agregar el directorio raíz al path para imports
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)


@pytest.fixture(scope="session")
def app_config():
    """Fixture que provee configuración de la aplicación para tests"""
    return {
        "window_size": (360, 720),
        "theme": "Green",
        "accent": "Amber",
    }


@pytest.fixture
def mock_user_data():
    """Fixture que provee datos de usuario de ejemplo"""
    return {
        "name": "Ana Martínez",
        "username": "ana_eco",
        "email": "ana@example.com",
        "ecotokens": 1250,
        "streak": 23,
        "recycled_items": 247,
        "co2_saved": 15.6,
        "level": 15,
        "rank": "Eco Champion"
    }


@pytest.fixture
def mock_achievement_data():
    """Fixture que provee datos de logros de ejemplo"""
    return [
        {
            "name": "Eco Warrior",
            "description": "Reciclaste 100 elementos",
            "progress": 100,
            "max_progress": 100,
            "rarity": "Oro",
            "completed": True
        },
        {
            "name": "Green Champion",
            "description": "Mantén una racha de 30 días",
            "progress": 23,
            "max_progress": 30,
            "rarity": "Plata",
            "completed": False
        }
    ]


@pytest.fixture
def mock_community_post():
    """Fixture que provee un post de comunidad de ejemplo"""
    return {
        "user": "Ana López",
        "rank": "Eco Champion",
        "time": "2h",
        "location": "Polanco, CDMX",
        "content": "¡Logré mi meta semanal! 25 botellas recicladas y 300 EcoTokens ganados 🌿",
        "badge": "Semana Verde Completada",
        "likes": 24,
        "comments": 5,
        "shares": 3
    }

