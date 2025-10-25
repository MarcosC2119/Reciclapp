"""
Script para inicializar datos de ejemplo en la base de datos
"""
from app.database.database import Database
from app.models.user import User


def create_sample_users():
    """Crea usuarios de ejemplo para testing"""
    db = Database()
    
    # Usuarios de ejemplo
    sample_users = [
        User(
            username="ana_eco",
            email="ana@example.com",
            password="123456",  # En producción, esto debería estar hasheado
            name="Ana Martínez",
            ecotokens=1250,
            streak=23,
            recycled_items=247,
            co2_saved=15.6,
            level=15,
            rank="Eco Champion"
        ),
        User(
            username="carlos_green",
            email="carlos@example.com",
            password="123456",
            name="Carlos Verde",
            ecotokens=850,
            streak=12,
            recycled_items=156,
            co2_saved=9.8,
            level=8,
            rank="Eco Warrior"
        ),
        User(
            username="maria_eco",
            email="maria@example.com",
            password="123456",
            name="María Eco",
            ecotokens=2100,
            streak=45,
            recycled_items=389,
            co2_saved=24.2,
            level=22,
            rank="Eco Master"
        )
    ]
    
    print("Creando usuarios de ejemplo...")
    
    for user in sample_users:
        # Verificar si el usuario ya existe
        existing_user = db.get_user_by_username(user.username)
        if not existing_user:
            created_user = db.create_user(user)
            if created_user:
                print(f"Usuario creado: {created_user.username} ({created_user.name})")
            else:
                print(f"Error al crear usuario: {user.username}")
        else:
            print(f"Usuario ya existe: {user.username}")
    
    print("\nUsuarios de ejemplo creados:")
    print("Username: ana_eco, Password: 123456")
    print("Username: carlos_green, Password: 123456")
    print("Username: maria_eco, Password: 123456")


if __name__ == "__main__":
    create_sample_users()
