"""
Sistema de Persistencia de Datos - Reciclapp
Autor: Marcos Castro (mcastro2024@alu.uct.cl)

Maneja el almacenamiento y carga de datos del usuario utilizando JSON.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional


class Database:
    """
    Clase para manejar la persistencia de datos de la aplicación.
    
    Utiliza JSON para almacenar:
    - Datos del usuario (nombre, email, eco_tokens, racha)
    - Historial de reciclaje
    - Logros desbloqueados
    - Configuración de la app
    """
    
    def __init__(self, data_dir: str = 'data'):
        """
        Inicializa la base de datos.
        
        Args:
            data_dir: Directorio donde se guardarán los archivos de datos
        """
        self.data_dir = data_dir
        self.data_file = os.path.join(data_dir, 'user_data.json')
        self.data: Dict[str, Any] = {}
        
        # Crear directorio si no existe
        os.makedirs(data_dir, exist_ok=True)
        
        # Cargar datos existentes o crear estructura inicial
        self.load_data()
    
    def load_data(self) -> None:
        """Carga los datos desde el archivo JSON."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
                print(f"✅ Datos cargados desde {self.data_file}")
            except json.JSONDecodeError:
                print(f"⚠️ Error al leer {self.data_file}, creando nueva estructura")
                self._create_initial_data()
        else:
            print(f"📝 Creando nueva base de datos en {self.data_file}")
            self._create_initial_data()
    
    def _create_initial_data(self) -> None:
        """Crea la estructura inicial de datos."""
        self.data = {
            'user': {
                'name': 'Usuario',
                'email': '',
                'eco_tokens': 0,
                'streak': 0,
                'level': 1,
                'total_recycled': 0,
                'joined_date': datetime.now().isoformat(),
                'last_login': datetime.now().isoformat()
            },
            'recycling_history': [],
            'achievements': [],
            'settings': {
                'notifications': True,
                'theme': 'light',
                'language': 'es'
            },
            'stats': {
                'total_items_recycled': 0,
                'total_co2_saved': 0,
                'total_water_saved': 0,
                'favorite_material': 'plastic'
            }
        }
        self.save_data()
    
    def save_data(self) -> bool:
        """
        Guarda los datos en el archivo JSON.
        
        Returns:
            True si se guardó exitosamente, False en caso contrario
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            print(f"💾 Datos guardados en {self.data_file}")
            return True
        except Exception as e:
            print(f"❌ Error al guardar datos: {e}")
            return False
    
    # ==================== MÉTODOS DE USUARIO ====================
    
    def get_user(self) -> Dict[str, Any]:
        """Obtiene los datos del usuario actual."""
        return self.data.get('user', {})
    
    def update_user(self, **kwargs) -> None:
        """
        Actualiza los datos del usuario.
        
        Args:
            **kwargs: Campos a actualizar (name, email, etc.)
        """
        for key, value in kwargs.items():
            if key in self.data['user']:
                self.data['user'][key] = value
        self.save_data()
    
    def update_last_login(self) -> None:
        """Actualiza la fecha del último inicio de sesión."""
        self.data['user']['last_login'] = datetime.now().isoformat()
        self.save_data()
    
    # ==================== MÉTODOS DE ECO-TOKENS ====================
    
    def get_eco_tokens(self) -> int:
        """Obtiene la cantidad actual de eco-tokens."""
        return self.data['user'].get('eco_tokens', 0)
    
    def add_eco_tokens(self, amount: int) -> int:
        """
        Añade eco-tokens al usuario.
        
        Args:
            amount: Cantidad de tokens a añadir
            
        Returns:
            Nueva cantidad total de eco-tokens
        """
        self.data['user']['eco_tokens'] += amount
        new_total = self.data['user']['eco_tokens']
        self.save_data()
        print(f"🪙 +{amount} eco-tokens. Total: {new_total}")
        return new_total
    
    def spend_eco_tokens(self, amount: int) -> bool:
        """
        Gasta eco-tokens del usuario.
        
        Args:
            amount: Cantidad de tokens a gastar
            
        Returns:
            True si se gastaron exitosamente, False si no hay suficientes
        """
        current = self.get_eco_tokens()
        if current >= amount:
            self.data['user']['eco_tokens'] -= amount
            self.save_data()
            print(f"💸 -{amount} eco-tokens. Restante: {self.data['user']['eco_tokens']}")
            return True
        else:
            print(f"❌ No hay suficientes eco-tokens. Tienes: {current}, necesitas: {amount}")
            return False
    
    # ==================== MÉTODOS DE RACHA ====================
    
    def get_streak(self) -> int:
        """Obtiene la racha actual del usuario."""
        return self.data['user'].get('streak', 0)
    
    def increment_streak(self) -> int:
        """
        Incrementa la racha del usuario en 1.
        
        Returns:
            Nueva racha
        """
        self.data['user']['streak'] += 1
        new_streak = self.data['user']['streak']
        self.save_data()
        print(f"🔥 Racha aumentada a {new_streak} días")
        return new_streak
    
    def reset_streak(self) -> None:
        """Resetea la racha a 0."""
        self.data['user']['streak'] = 0
        self.save_data()
        print("💔 Racha reseteada a 0")
    
    # ==================== MÉTODOS DE RECICLAJE ====================
    
    def add_recycling_item(self, material: str, quantity: int = 1, eco_tokens: int = 10) -> None:
        """
        Registra un item reciclado.
        
        Args:
            material: Tipo de material (plastic, paper, glass, metal, organic)
            quantity: Cantidad de items
            eco_tokens: Tokens ganados
        """
        item = {
            'date': datetime.now().isoformat(),
            'material': material,
            'quantity': quantity,
            'eco_tokens': eco_tokens
        }
        
        self.data['recycling_history'].append(item)
        self.data['user']['total_recycled'] += quantity
        self.data['stats']['total_items_recycled'] += quantity
        
        # Añadir eco-tokens
        self.add_eco_tokens(eco_tokens)
        
        # Actualizar estadísticas
        self._update_environmental_impact(material, quantity)
        
        self.save_data()
        print(f"♻️ Item reciclado: {quantity}x {material} (+{eco_tokens} tokens)")
    
    def _update_environmental_impact(self, material: str, quantity: int) -> None:
        """
        Actualiza las estadísticas de impacto ambiental.
        
        Args:
            material: Tipo de material
            quantity: Cantidad
        """
        # Valores aproximados de impacto por material
        impact_values = {
            'plastic': {'co2': 2.5, 'water': 15},
            'paper': {'co2': 1.5, 'water': 25},
            'glass': {'co2': 0.8, 'water': 5},
            'metal': {'co2': 3.5, 'water': 10},
            'organic': {'co2': 0.5, 'water': 2}
        }
        
        if material in impact_values:
            self.data['stats']['total_co2_saved'] += impact_values[material]['co2'] * quantity
            self.data['stats']['total_water_saved'] += impact_values[material]['water'] * quantity
    
    def get_recycling_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Obtiene el historial de reciclaje.
        
        Args:
            limit: Número máximo de items a retornar (None para todos)
            
        Returns:
            Lista de items reciclados
        """
        history = self.data.get('recycling_history', [])
        if limit:
            return history[-limit:]
        return history
    
    # ==================== MÉTODOS DE LOGROS ====================
    
    def unlock_achievement(self, achievement_id: str, name: str, description: str) -> bool:
        """
        Desbloquea un logro.
        
        Args:
            achievement_id: ID único del logro
            name: Nombre del logro
            description: Descripción del logro
            
        Returns:
            True si se desbloqueó ahora, False si ya estaba desbloqueado
        """
        # Verificar si ya está desbloqueado
        if any(a['id'] == achievement_id for a in self.data['achievements']):
            return False
        
        achievement = {
            'id': achievement_id,
            'name': name,
            'description': description,
            'unlocked_date': datetime.now().isoformat()
        }
        
        self.data['achievements'].append(achievement)
        self.save_data()
        print(f"🏆 Logro desbloqueado: {name}")
        return True
    
    def get_achievements(self) -> List[Dict[str, Any]]:
        """Obtiene todos los logros desbloqueados."""
        return self.data.get('achievements', [])
    
    # ==================== MÉTODOS DE ESTADÍSTICAS ====================
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtiene las estadísticas del usuario."""
        return self.data.get('stats', {})
    
    def get_total_items_recycled(self) -> int:
        """Obtiene el total de items reciclados."""
        return self.data['stats'].get('total_items_recycled', 0)
    
    def get_environmental_impact(self) -> Dict[str, float]:
        """
        Obtiene el impacto ambiental del usuario.
        
        Returns:
            Diccionario con CO2 y agua ahorrados
        """
        return {
            'co2_saved': self.data['stats'].get('total_co2_saved', 0),
            'water_saved': self.data['stats'].get('total_water_saved', 0)
        }
    
    # ==================== MÉTODOS GENERALES ====================
    
    def reset_all_data(self) -> None:
        """Resetea todos los datos a los valores iniciales (¡CUIDADO!)."""
        self._create_initial_data()
        print("⚠️ Todos los datos han sido reseteados")
    
    def export_data(self, filepath: str) -> bool:
        """
        Exporta los datos a un archivo JSON específico.
        
        Args:
            filepath: Ruta del archivo de destino
            
        Returns:
            True si se exportó exitosamente
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            print(f"📤 Datos exportados a {filepath}")
            return True
        except Exception as e:
            print(f"❌ Error al exportar: {e}")
            return False
