"""
Sistema de Analytics y Métricas - Reciclapp
Autor: Marcos Castro (mcastro2024@alu.uct.cl)

Maneja el tracking de eventos y métricas de uso de la aplicación.
Cumple con el RA3: Evaluación de funcionalidad mediante métricas.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional


class Analytics:
    """
    Clase para tracking de eventos y análisis de comportamiento de usuarios.
    
    Trackea:
    - Eventos de la aplicación (clicks, navegación, acciones)
    - Sesiones de usuario (inicio, fin, duración)
    - Uso de features
    - Comportamiento del usuario
    """
    
    def __init__(self, data_dir: str = 'data'):
        """
        Inicializa el sistema de analytics.
        
        Args:
            data_dir: Directorio donde se guardarán los eventos
        """
        self.data_dir = data_dir
        self.events_file = os.path.join(data_dir, 'events.json')
        self.events: List[Dict[str, Any]] = []
        self.current_session: Optional[Dict[str, Any]] = None
        
        # Crear directorio si no existe
        os.makedirs(data_dir, exist_ok=True)
        
        # Cargar eventos existentes
        self.load_events()
    
    def load_events(self) -> None:
        """Carga los eventos desde el archivo JSON."""
        if os.path.exists(self.events_file):
            try:
                with open(self.events_file, 'r', encoding='utf-8') as f:
                    self.events = json.load(f)
                print(f"[STATS] {len(self.events)} eventos cargados")
            except json.JSONDecodeError:
                print(f"[WARNING] Error al leer eventos, creando nuevo archivo")
                self.events = []
        else:
            print(f"[INFO] Creando nuevo archivo de eventos")
            self.events = []
    
    def save_events(self) -> bool:
        """
        Guarda los eventos en el archivo JSON.
        
        Returns:
            True si se guardó exitosamente
        """
        try:
            with open(self.events_file, 'w', encoding='utf-8') as f:
                json.dump(self.events, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"[ERROR] Error al guardar eventos: {e}")
            return False
    
    # ==================== TRACKING DE EVENTOS ====================
    
    def track_event(self, event_name: str, properties: Optional[Dict[str, Any]] = None) -> None:
        """
        Registra un evento.
        
        Args:
            event_name: Nombre del evento (ej: 'button_click', 'screen_view')
            properties: Propiedades adicionales del evento
        """
        event = {
            'timestamp': datetime.now().isoformat(),
            'event': event_name,
            'properties': properties or {},
            'session_id': self.current_session['id'] if self.current_session else None
        }
        
        self.events.append(event)
        self.save_events()
        
        # Log en consola para debugging
        props_str = f" - {properties}" if properties else ""
        print(f"[EVENT] Event: {event_name}{props_str}")
    
    def track_screen_view(self, screen_name: str) -> None:
        """
        Registra la vista de una pantalla.
        
        Args:
            screen_name: Nombre de la pantalla
        """
        self.track_event('screen_view', {'screen': screen_name})
    
    def track_button_click(self, button_name: str, screen: Optional[str] = None) -> None:
        """
        Registra el click en un botón.
        
        Args:
            button_name: Nombre del botón
            screen: Pantalla donde se hizo click
        """
        properties = {'button': button_name}
        if screen:
            properties['screen'] = screen
        
        self.track_event('button_click', properties)
    
    def track_recycling_action(self, material: str, quantity: int, tokens_earned: int) -> None:
        """
        Registra una acción de reciclaje.
        
        Args:
            material: Tipo de material reciclado
            quantity: Cantidad
            tokens_earned: Tokens ganados
        """
        self.track_event('recycling_logged', {
            'material': material,
            'quantity': quantity,
            'tokens_earned': tokens_earned
        })
    
    def track_achievement_unlocked(self, achievement_id: str, achievement_name: str) -> None:
        """
        Registra el desbloqueo de un logro.
        
        Args:
            achievement_id: ID del logro
            achievement_name: Nombre del logro
        """
        self.track_event('achievement_unlocked', {
            'achievement_id': achievement_id,
            'achievement_name': achievement_name
        })
    
    def track_login(self, method: str = 'email') -> None:
        """
        Registra un inicio de sesión.
        
        Args:
            method: Método de login (email, google, etc.)
        """
        self.track_event('login', {'method': method})
    
    # ==================== SESIONES ====================
    
    def start_session(self) -> str:
        """
        Inicia una nueva sesión de usuario.
        
        Returns:
            ID de la sesión
        """
        session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        self.current_session = {
            'id': session_id,
            'start_time': datetime.now().isoformat(),
            'end_time': None,
            'duration': None
        }
        
        self.track_event('session_start', {'session_id': session_id})
        print(f"[SESSION_START] Sesión iniciada: {session_id}")
        
        return session_id
    
    def end_session(self) -> Optional[float]:
        """
        Finaliza la sesión actual.
        
        Returns:
            Duración de la sesión en segundos, o None si no hay sesión activa
        """
        if not self.current_session:
            print("[WARNING] No hay sesión activa para finalizar")
            return None
        
        end_time = datetime.now()
        start_time = datetime.fromisoformat(self.current_session['start_time'])
        duration = (end_time - start_time).total_seconds()
        
        self.current_session['end_time'] = end_time.isoformat()
        self.current_session['duration'] = duration
        
        self.track_event('session_end', {
            'session_id': self.current_session['id'],
            'duration_seconds': duration,
            'duration_minutes': round(duration / 60, 2)
        })
        
        print(f"[SESSION_END] Sesión finalizada: {duration:.2f}s ({duration/60:.2f}min)")
        
        session_duration = duration
        self.current_session = None
        
        return session_duration
    
    def get_session_duration(self) -> Optional[float]:
        """
        Obtiene la duración actual de la sesión.
        
        Returns:
            Duración en segundos, o None si no hay sesión activa
        """
        if not self.current_session:
            return None
        
        start_time = datetime.fromisoformat(self.current_session['start_time'])
        current_time = datetime.now()
        duration = (current_time - start_time).total_seconds()
        
        return duration
    
    # ==================== ANÁLISIS DE DATOS ====================
    
    def get_event_count(self, event_name: Optional[str] = None) -> int:
        """
        Obtiene la cantidad de eventos.
        
        Args:
            event_name: Nombre del evento específico (None para todos)
            
        Returns:
            Cantidad de eventos
        """
        if event_name:
            return sum(1 for e in self.events if e['event'] == event_name)
        return len(self.events)
    
    def get_most_viewed_screens(self, limit: int = 5) -> List[tuple[str, int]]:
        """
        Obtiene las pantallas más vistas.
        
        Args:
            limit: Número de resultados a retornar
            
        Returns:
            Lista de tuplas (screen_name, count)
        """
        screen_views = {}
        
        for event in self.events:
            if event['event'] == 'screen_view':
                screen = event['properties'].get('screen', 'unknown')
                screen_views[screen] = screen_views.get(screen, 0) + 1
        
        # Ordenar por cantidad y retornar el top
        sorted_screens = sorted(screen_views.items(), key=lambda x: x[1], reverse=True)
        return sorted_screens[:limit]
    
    def get_most_clicked_buttons(self, limit: int = 10) -> List[tuple[str, int]]:
        """
        Obtiene los botones más clickeados.
        
        Args:
            limit: Número de resultados a retornar
            
        Returns:
            Lista de tuplas (button_name, count)
        """
        button_clicks = {}
        
        for event in self.events:
            if event['event'] == 'button_click':
                button = event['properties'].get('button', 'unknown')
                button_clicks[button] = button_clicks.get(button, 0) + 1
        
        sorted_buttons = sorted(button_clicks.items(), key=lambda x: x[1], reverse=True)
        return sorted_buttons[:limit]
    
    def get_total_recycling_items(self) -> int:
        """
        Obtiene el total de items reciclados (desde eventos).
        
        Returns:
            Total de items
        """
        total = 0
        for event in self.events:
            if event['event'] == 'recycling_logged':
                total += event['properties'].get('quantity', 0)
        return total
    
    def get_recycling_by_material(self) -> Dict[str, int]:
        """
        Obtiene la cantidad de items reciclados por tipo de material.
        
        Returns:
            Diccionario {material: quantity}
        """
        materials = {}
        
        for event in self.events:
            if event['event'] == 'recycling_logged':
                material = event['properties'].get('material', 'unknown')
                quantity = event['properties'].get('quantity', 0)
                materials[material] = materials.get(material, 0) + quantity
        
        return materials
    
    def get_average_session_duration(self) -> float:
        """
        Obtiene la duración promedio de las sesiones.
        
        Returns:
            Duración promedio en segundos
        """
        session_ends = [e for e in self.events if e['event'] == 'session_end']
        
        if not session_ends:
            return 0.0
        
        total_duration = sum(e['properties'].get('duration_seconds', 0) for e in session_ends)
        return total_duration / len(session_ends)
    
    def get_total_sessions(self) -> int:
        """
        Obtiene el número total de sesiones.
        
        Returns:
            Cantidad de sesiones
        """
        return self.get_event_count('session_start')
    
    # ==================== REPORTES ====================
    
    def generate_summary_report(self) -> Dict[str, Any]:
        """
        Genera un reporte resumen de todas las métricas.
        
        Returns:
            Diccionario con el resumen de métricas
        """
        report = {
            'total_events': len(self.events),
            'total_sessions': self.get_total_sessions(),
            'average_session_duration_seconds': self.get_average_session_duration(),
            'average_session_duration_minutes': round(self.get_average_session_duration() / 60, 2),
            'total_screen_views': self.get_event_count('screen_view'),
            'total_button_clicks': self.get_event_count('button_click'),
            'total_recycling_events': self.get_event_count('recycling_logged'),
            'total_items_recycled': self.get_total_recycling_items(),
            'most_viewed_screens': self.get_most_viewed_screens(5),
            'most_clicked_buttons': self.get_most_clicked_buttons(5),
            'recycling_by_material': self.get_recycling_by_material(),
            'achievements_unlocked': self.get_event_count('achievement_unlocked')
        }
        
        return report
    
    def print_summary_report(self) -> None:
        """Imprime un reporte resumen en consola."""
        report = self.generate_summary_report()
        
        print("\n" + "="*50)
        print("📊 REPORTE DE MÉTRICAS - RECICLAPP")
        print("="*50)
        print(f"\n[STATS] Eventos Totales: {report['total_events']}")
        print(f"[STATS] Sesiones Totales: {report['total_sessions']}")
        print(f"[STATS] Duración Promedio de Sesión: {report['average_session_duration_minutes']} min")
        print(f"[STATS] Vistas de Pantallas: {report['total_screen_views']}")
        print(f"[STATS] Clicks en Botones: {report['total_button_clicks']}")
        print(f"[STATS] Items Reciclados: {report['total_items_recycled']}")
        print(f"[STATS] Logros Desbloqueados: {report['achievements_unlocked']}")
        
        print("\n[TOP] Top 5 Pantallas Más Vistas:")
        for screen, count in report['most_viewed_screens']:
            print(f"   - {screen}: {count} vistas")
        
        print("\n[TOP] Top 5 Botones Más Clickeados:")
        for button, count in report['most_clicked_buttons'][:5]:
            print(f"   - {button}: {count} clicks")
        
        print("\n[STATS] Reciclaje por Material:")
        for material, quantity in report['recycling_by_material'].items():
            print(f"   - {material}: {quantity} items")
        
        print("="*50 + "\n")
    
    def export_report(self, filepath: str) -> bool:
        """
        Exporta el reporte a un archivo JSON.
        
        Args:
            filepath: Ruta del archivo de destino
            
        Returns:
            True si se exportó exitosamente
        """
        try:
            report = self.generate_summary_report()
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=4, ensure_ascii=False)
            print(f"[EXPORT] Reporte exportado a {filepath}")
            return True
        except Exception as e:
            print(f"[ERROR] Error al exportar reporte: {e}")
            return False
    
    # ==================== LIMPIEZA ====================
    
    def clear_old_events(self, days: int = 30) -> int:
        """
        Elimina eventos más antiguos que X días.
        
        Args:
            days: Días a mantener
            
        Returns:
            Cantidad de eventos eliminados
        """
        cutoff_date = datetime.now().timestamp() - (days * 24 * 60 * 60)
        
        original_count = len(self.events)
        self.events = [
            e for e in self.events 
            if datetime.fromisoformat(e['timestamp']).timestamp() > cutoff_date
        ]
        
        deleted = original_count - len(self.events)
        if deleted > 0:
            self.save_events()
            print(f"[CLEANUP] {deleted} eventos antiguos eliminados")
        
        return deleted
