# Uso de Inteligencia Artificial en el Desarrollo de Reciclapp

**Proyecto:** Reciclapp - Aplicación de Reciclaje con Gamificación  
**Desarrollador:** Marcos Castro (mcastro2024@alu.uct.cl)  
**Fecha:** Noviembre 2024

---

## 📋 Resumen Ejecutivo

Este documento detalla el uso de herramientas de Inteligencia Artificial durante el desarrollo de Reciclapp, cumpliendo con los requisitos de transparencia de la Evaluación N°6.

---

## 🤖 Herramientas de IA Utilizadas

### 1. Google Gemini (Principal)
- **Versión:** Gemini 1.5 / Gemini 2.0
- **Uso:** Asistente principal de desarrollo
- **Porcentaje de influencia:** ~60-70% del código base

### 2. Otras herramientas
- **GitHub Copilot:** Autocompletado de código (si aplica)
- **ChatGPT:** Consultas específicas (si aplica)

---

## 📝 Áreas donde se Utilizó IA

### A. Arquitectura y Estructura del Proyecto

**Prompt utilizado:**
```
"Necesito crear una aplicación móvil con Kivy/KivyMD que siga el patrón 
de separación de diseño (.kv) y lógica (.py). Dame una estructura 
de proyecto profesional para una app de reciclaje."
```

**Resultado generado por IA:**
- Estructura de carpetas (`app/`, `screens/`, `components/`)
- Separación .kv / .py
- Sistema de navegación con ScreenManager

**Modificaciones realizadas:**
- Adaptación de nombres de pantallas específicos para Reciclapp
- Adición de templates personalizados
- Configuración del tema Green/Amber

---

### B. Sistema de Persistencia de Datos (`database.py`)

**Prompt utilizado:**
```
"Crea un sistema de persistencia de datos con JSON para una app de 
reciclaje que maneje: datos de usuario, eco-tokens, racha diaria, 
historial de reciclaje, logros y estadísticas de impacto ambiental."
```

**Código generado por IA:**
- Clase `Database` completa (~90% generada por IA)
- Métodos CRUD para usuario, eco-tokens, racha
- Sistema de historial de reciclaje
- Cálculo de impacto ambiental (CO2, agua)

**Modificaciones realizadas:**
- Ajuste de valores de impacto ambiental (CO2 y agua por material)
- Personalización de mensajes de consola con emojis
- Añadidura del nombre y email del desarrollador en comentarios
- Adaptación de la estructura de datos JSON inicial

---

### C. Sistema de Analytics (`analytics.py`)

**Prompt utilizado:**
```
"Implementa un sistema de analytics y métricas para cumplir con el RA3 
de mi evaluación. Debe trackear eventos, sesiones, clicks, vistas de 
pantallas y generar reportes de uso."
```

**Código generado por IA:**
- Clase `Analytics` completa (~85% generada por IA)
- Tracking de eventos (button_click, screen_view, etc.)
- Gestión de sesiones con duración
- Reportes y análisis de datos

**Modificaciones realizadas:**
- Añadidura de métodos específicos para eventos de reciclaje
- Personalización de reportes en consola
- Integración con el sistema de logros

---

### D. Integración en Pantallas

**Prompts utilizados:**
```
"Integra el sistema de database y analytics en home_screen.py para 
que el botón de escanear QR simule reciclaje, añada eco-tokens y 
trackee el evento."

"Añade tracking de analytics en todas las acciones de navegación 
y botones en las pantallas."
```

**Código generado por IA:**
- Método `escanear_qr()` con simulación de reciclaje (~80% IA)
- Sistema de logros automáticos (`check_achievements()`) (~90% IA)
- Tracking en `login_screen.py` y `profile_screen.py` (~70% IA)

**Modificaciones realizadas:**
- Añadidura de `update_dashboard_data()` personalizado
- Ajuste de mensajes de consola
- Vinculación con la UI de Kivy/KivyMD

---

### E. Diseño de Interfaz (Archivos .kv)

**Uso de IA:** Mínimo (~20%)

**Prompts utilizados:**
```
"Dame un ejemplo de diseño KivyMD para una pantalla de inicio con 
estadísticas, botones de acción rápida y navegación inferior."
```

**Resultado:**
- Estructura básica de layouts
- Ejemplos de componentes MDCard, MDLabel, etc.

**Modificaciones realizadas:**
- **Diseño visual completo hecho manual mente (80%)**
- Colores personalizados para Reciclapp
- Navegación inferior con botón QR central
- Adaptación de todas las pantallas (welcome, login, home, profile, etc.)

---

## 🔧 Código Escrito Completamente por el Desarrollador

### Sin uso de IA:
1. **Diseño visual de pantallas (.kv)** - 70-80% manual
2. **Configuración de tema en main.py** - 100% manual
3. **Nombres y textos en español** - 100% manual
4. **Testing manual y debugging** - 100% manual
5. **Estructura de carpetas final** - Personalizada

---

## 📊 Proporción de Código: IA vs Manual

| Componente | IA | Manual | Modificaciones |
|------------|----|----|----------------|
| `database.py` | 90% | 10% | Valores de impacto, mensajes |
| `analytics.py` | 85% | 15% | Métodos personalizados |
| `main.py` | 70% | 30% | Integración y configuración |
| `home_screen.py` | 80% | 20% | Lógica de negocio específica |
| `login_screen.py` | 70% | 30% | Tracking y persistencia |
| `profile_screen.py` | 60% | 40% | Métodos personalizados |
| **Archivos .kv** | 20% | 80% | Diseño visual completo |
| **Testing** | 50% | 50% | Estructura IA, tests manuales |
| **Documentación** | 40% | 60% | README y guías |

**Promedio general:** ~60% generado por IA, ~40% desarrollo manual

---

## ✅ Proceso de Trabajo con IA

### 1. Prompt Inicial
Descripción clara del problema o funcionalidad necesaria

### 2. Recepción del Código
Revisión y análisis del código generado por IA

### 3. Testing
Pruebas del código para verificar funcionamiento

### 4. Modificación
Ajustes y personalizaciones según necesidades específicas

### 5. Integración
Vincular el código con el resto de la aplicación

### 6. Documentación
Escribir comentarios y documentación del código

---

## 🎓 Aprendizajes del Uso de IA

### Ventajas:
✅ Aceleración del desarrollo (3-4x más rápido)  
✅ Código bien estructurado y profesional  
✅ Aprendizaje de mejores prácticas  
✅ Generación de documentación base  
✅ Solución de problemas técnicos complejos

### Desventajas:
❌ Necesidad de revisión constante del código  
❌ Algunas soluciones genéricas que requieren personalización  
❌ Dependencia para resolver problemas nuevos  
❌ Código a veces sobre-ingenierizado

### Lecciones Aprendidas:
1. **La IA es una herramienta, no un reemplazo** - Requiere supervisión humana
2. **Entender el código generado es crucial** - No solo copiar y pegar
3. **Prompts específicos = mejores resultados** - Claridad en las solicitudes
4. **Testing es imprescindible** - El código de IA puede tener errores
5. **Personalización es clave** - Adaptación a necesidades específicas

---

## 🔍 Ejemplo Detallado: Sistema de Logros

### Prompt Original:
```
"Crea un sistema para verificar y desbloquear logros automáticamente 
basado en el progreso del usuario (items reciclados, eco-tokens, racha)."
```

### Código Generado por IA:
```python
def check_achievements(self):
    app = MDApp.get_running_app()
    
    eco_tokens = app.db.get_eco_tokens()
    total_recycled = app.db.get_total_items_recycled()
    
    if total_recycled >= 10:
        app.db.unlock_achievement('eco_warrior', 'Eco Guerrero', 'Reciclaste 10 items')
```

### Código Modificado por Mí:
```python
def check_achievements(self):
    """Verifica y desbloquea logros basados en el progreso"""  # ← Añadido
    app = MDApp.get_running_app()
    
    eco_tokens = app.db.get_eco_tokens()
    total_recycled = app.db.get_total_items_recycled()
    streak = app.db.get_streak()  # ← Añadido
    
    # Logro: Primer reciclaje  # ← Añadido
    if total_recycled >= 1:  # ← Modificado
        unlocked = app.db.unlock_achievement(
            'first_recycle',  # ← Modificado
            'Primer Paso',  # ← Modificado
            'Reciclaste tu primer item'  # ← Modificado
        )
        if unlocked:  # ← Añadido
            app.analytics.track_achievement_unlocked('first_recycle', 'Primer Paso')
    
    # ... más logros personalizados
```

**Cambios realizados:**
- Docstring descriptivo
- Tracking de racha adicional
- Logro para primer item (umbral más bajo)
- IDs y nombres de logros en español
- Integración con analytics

---

## 📌 Declaración de Transparencia

**Confirmo que:**
1. He utilizado IA (principalmente Google Gemini) como herramienta de asistencia
2. Todo el código generado ha sido revisado y comprendido
3. He realizado modificaciones significativas (40% del código total)
4. El diseño visual es mayoritariamente trabajo manual
5. Asumo responsabilidad completa por el funcionamiento de la aplicación

**Firma Digital:**  
Marcos Castro  
mcastro2024@alu.uct.cl  
Noviembre 2024
