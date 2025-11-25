# Desafíos de Desarrollo - Reciclapp

**Proyecto:** Reciclapp - Aplicación Móvil de Reciclaje  
**Desarrollador:** Marcos Castro (mcastro2024@alu.uct.cl)  
**Framework:** Kivy / KivyMD  
**Período:** Semestre 2024

---

## 📋 Índice

1. [Contexto del Proyecto](#contexto)
2. [Decisiones Técnicas Principales](#decisiones-técnicas)
3. [Desafíos Enfrentados](#desafíos)
4. [Soluciones Implementadas](#soluciones)
5. [Lecciones Aprendidas](#lecciones)

---

## 🎯 Contexto del Proyecto {#contexto}

### Objetivo
Desarrollar una aplicación móvil que gamifique el reciclaje, motivando a los usuarios mediante:
- Sistema de recompensas (eco-tokens)
- Rachas diarias
- Logros desbloqueables
- Impacto ambiental visible

### Requisitos Técnicos
- **Framework:** Kivy 2.3.1 + KivyMD 1.2.0
- **Lenguaje:** Python 3.12
- **Arquitectura:** Separación .kv (diseño) / .py (lógica)
- **Persistencia:** JSON
- **Métricas:** Sistema de analytics propio

---

## 🔧 Decisiones Técnicas Principales {#decisiones-técnicas}

### 1. ¿Por qué Kivy/KivyMD?

**Decisión:** Usar Kivy con Material Design (KivyMD)

**Razones:**
- ✅ Requisito del curso
- ✅ Multiplataforma (Android, iOS, Desktop)
- ✅ Diseño moderno con Material Design
- ✅ Desarrollo rápido con lenguaje .kv

**Desafíos anticipados:**
- ⚠️ Curva de aprendizaje de lenguaje .kv
- ⚠️ Documentación limitada en español
- ⚠️ Debugging más complejo que frameworks nativos

---

### 2. Arquitectura: Separación de Responsabilidades

**Decisión:** Separar completamente diseño (.kv) y lógica (.py)

**Estructura adoptada:**
```
app/
├── main.py                    # Aplicación principal
├── main.kv                    # Diseño principal
├── database.py                # Persistencia
├── analytics.py               # Métricas
└── screens/
    ├── home_screen.py         # Lógica
    └── home_screen.kv         # Diseño
```

**Ventajas:**
- ✅ Código más limpio y organizado
- ✅ Facilita el mantenimiento
- ✅ Permite trabajo paralelo en diseño y lógica
- ✅ Reutilización de componentes

**Desventajas:**
- ❌ Más archivos que gestionar
- ❌ Sincronización entre .kv y .py
- ❌ IDs deben estar bien definidos

---

### 3. Persistencia de Datos: JSON vs SQLite

**Decisión:** Utilizar JSON para persistencia

#### Análisis de Alternativas

| Criterio | JSON | SQLite |
|----------|------|--------|
| Facilidad de implementación | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Portabilidad | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Velocidad de lectura | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Escalabilidad | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Debugging | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Tamaño del proyecto | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**Justificación de JSON:**
1. **Simplicidad:** No requiere librerías adicionales
2. **Legibilidad:** Archivos fáciles de leer y editar
3. **Portabilidad:** Compatible con cualquier plataforma
4. **Alcance:** Suficiente para ~100-1000 usuarios
5. **Tiempo:** Desarrollo más rápido para MVP

**Cuándo usar SQLite:**
- Más de 10,000 registros
- Queries complejas con JOINs
- Múltiples tablas relacionadas
- Actualización de producción

---

### 4. Sistema de Métricas: Propio vs Externo

**Decisión:** Implementar sistema de analytics propio

**Alternativas consideradas:**
- Firebase Analytics (requiere cuenta y configuración)
- Google Analytics (overhead innecesario)
- Sistema propio (control total)

**Ventajas del sistema propio:**
- ✅ Control total sobre qué se trackea
- ✅ Sin dependencias externas
- ✅ Datos guardados localmente
- ✅ Cumple perfectamente con RA3
- ✅ Privacidad del usuario

**Características implementadas:**
- Tracking de eventos (clicks, navegación)
- Sesiones con duración
- Reportes resumidos
- Análisis de comportamiento

---

## 🚧 Desafíos Enfrentados {#desafíos}

### Desafío 1: Entender el Lenguaje .kv

**Problema:**  
El lenguaje .kv de Kivy es declarativo y muy diferente a Python. Inicialmente era difícil entender la sintaxis y la forma de vincular acciones.

**Síntomas:**
- Errores de sintaxis sin mensajes claros
- No saber cómo vincular botones con métodos
- Confusión con propiedades y bindings

**Ejemplo del error:**
```kv
# ❌ INCORRECTO - Yo intentaba:
Button:
    text: "Click"
    on_press: self.mi_metodo()  # ← Paréntesis causan error

# ✅ CORRECTO - Debía ser:
Button:
    text: "Click"
    on_press: root.mi_metodo()  # ← Sin paréntesis, usar 'root'
```

**Solución:**
1. Estudiar documentación oficial de Kivy
2. Probar ejemplos pequeños incrementalmente
3. Usar `print()` para debugging
4. Entender diferencia entre `self`, `root` y `app`

**Tiempo invertido:** ~4 horas

---

### Desafío 2: Navegación entre Pantallas

**Problema:**  
Implementar navegación fluida entre 6 pantallas diferentes con navbar inferior persistente.

**Requisitos:**
- Navbar visible solo en ciertas pantallas (home, community, achievements, profile)
- Navbar oculto en welcome y login
- Botón QR central en el navbar
- Resaltar botón activo

**Solución implementada:**
```kv
# Navbar con visibilidad condicional
FloatLayout:
    opacity: 1 if screen_manager.current in ['home', 'community'] else 0
    disabled: screen_manager.current not in ['home', 'community']
```

**Desafíos secundarios:**
- Posicionamiento del botón QR central
- Cambio de color del botón activo
- Sincronización con ScreenManager

**Tiempo invertido:** ~3 horas

---

### Desafío 3: Integración de Database y Analytics

**Problema:**  
Hacer que todas las pantallas tengan acceso a `Database` y `Analytics` sin pasar referencias manualmente.

**Primera aproximación (incorrecta):**
```python
# ❌ Pasar como parámetros - Muy verboso
class HomeScreen(MDScreen):
    def __init__(self, db, analytics, **kwargs):
        self.db = db
        self.analytics = analytics
```

**Solución final (correcta):**
```python
# ✅ Usar MDApp.get_running_app()
class HomeScreen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.db.get_eco_tokens()
        app.analytics.track_screen_view('home')
```

**Lección aprendida:**  
Kivy/MDApp es un singleton accesible desde cualquier pantalla.

**Tiempo invertido:** ~2 horas

---

### Desafío 4: Simulación de Escaneo QR

**Problema:**  
Implementar escaneo QR real requiere permisos de cámara y configuración compleja en móvil.

**Decisión:**  
Simular el escaneo con datos aleatorios para demostrar funcionalidad.

**Implementación:**
```python
def escanear_qr(self):
    materials = ['plastic', 'paper', 'glass', 'metal', 'organic']
    material = random.choice(materials)
    quantity = random.randint(1, 5)
    eco_tokens = quantity * 10
    
    app.db.add_recycling_item(material, quantity, eco_tokens)
```

**Justificación:**
- ✅ Demuestra el flujo completo
- ✅ Permite testing sin hardware
- ✅ Fácil de reemplazar con scanner real luego

---

### Desafío 5: Testing en Kivy

**Problema:**  
Los tests en Kivy son más complejos que en Python estándar porque requieren simular la aplicación gráfica.

**Desafíos específicos:**
- Inicializar la app en tests
- Simular clicks en botones
- Verificar cambios en la UI
- Tests asíncronos

**Solución con pytest:**
```python
@pytest.fixture
def app():
    from app.main import MainApp
    app_instance = MainApp()
    yield app_instance
    app_instance.stop()

def test_screen_navigation(app):
    app.root.current = 'home'
    assert app.root.current == 'home'
```

**Cobertura lograda:** ~80%

**Tiempo invertido:** ~5 horas

---

### Desafío 6: Diseño Responsive

**Problema:**  
La app debe verse bien en diferentes tamaños de pantalla (smartphones de distintos tamaños).

**Solución:**
- Usar `dp` (density-independent pixels) en lugar de pixels fijos
- Usar `size_hint` para layouts adaptativos
- Configurar ventana con aspecto 18:9 (moderno)

```python
# Configuración inicial
Window.size = (360, 720)  # Aspecto smartphone moderno
```

```kv
# Usar dp y size_hint
MDCard:
    size_hint: None, None
    size: dp(320), dp(200)  # ← Escala automáticamente
```

---

## ✅ Soluciones Implementadas {#soluciones}

### 1. Sistema de Persistencia Completo

**Características:**
- Guardar/cargar automático
- Estructura JSON clara y legible
- Métodos específicos para cada tipo de dato
- Manejo de errores robusto

**Código clave:**
```python
class Database:
    def save_data(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
```

---

### 2. Sistema de Métricas/Analytics

**Características:**
- Tracking automático de eventos
- Sesiones con duración
- Reportes en consola
- Exportación a JSON

**Eventos trackeados:**
- `app_start` - Inicio de app
- `screen_view` - Vista de pantalla
- `button_click` - Click en botón
- `login` - Inicio de sesión
- `recycling_logged` - Item reciclado
- `achievement_unlocked` - Logro desbloqueado

---

### 3. Sistema de Logros Automáticos

**Funcionamiento:**
1. Cada vez que se recicla un item, se llama `check_achievements()`
2. Se verifican umbrales (tokens, items, racha)
3. Se desbloquean logros si se cumplen condiciones
4. Se trackea el evento en Analytics

**Logros implementados:**
- "Primer Paso": 1 item reciclado
- "Eco Guerrero": 10 items reciclados
- "Coleccionista": 100 eco-tokens
- "Semana Completa": 7 días de racha

---

## 🎓 Lecciones Aprendidas {#lecciones}

### 1. Importancia de la Arquitectura

**Lección:**  
Invertir tiempo en diseñar una buena arquitectura ahorra mucho tiempo después.

**Aplicación:**
- Separar .kv y .py desde el inicio
- Crear módulos independientes (database, analytics)
- Usar patrones de diseño apropiados

---

### 2. Documentación es Crucial

**Lección:**  
Código sin documentación es código que olvidarás en 2 semanas.

**Aplicación:**
- Docstrings en todas las funciones
- README detallado
- Comentarios en código complejo
- Documentos de diseño

---

### 3. Testing Temprano

**Lección:**  
Testear desde el principio evita bugs acumulados.

**Aplicación:**
- pytest configurado desde día 1
- Tests unitarios para cada módulo
- Coverage como métrica de calidad

---

### 4. Commits Frecuentes

**Lección:**  
Commits pequeños y frecuentes son mejores que commits gigantes.

**Buenas prácticas adoptadas:**
- Commits cada feature completado
- Mensajes descriptivos en español/inglés
- Branches para features grandes

---

### 5. El Valor de la IA como Herramienta

**Lección:**  
La IA acelera el desarrollo pero NO reemplaza el entendimiento.

**Balance encontrado:**
- Usar IA para estructura inicial
- Modificar y personalizar siempre
- Entender cada línea de código
- Testear exhaustivamente

---

## 📊 Métricas del Desarrollo

### Tiempo Invertido

| Actividad | Horas | Porcentaje |
|-----------|-------|------------|
| Aprendizaje Kivy/KivyMD | 8h | 20% |
| Diseño de UI (.kv) | 10h | 25% |
| Lógica de negocio (.py) | 8h | 20% |
| Persistencia y Analytics | 6h | 15% |
| Testing | 4h | 10% |
| Documentación | 4h | 10% |
| **TOTAL** | **40h** | **100%** |

### Líneas de Código

| Archivo | Líneas | Complejidad |
|---------|--------|-------------|
| `database.py` | 338 | Alta |
| `analytics.py` | 410 | Alta |
| `main.py` | 94 | Media |
| `home_screen.py` | 170 | Media |
| `*.kv` files | ~1500 | Media |
| **TOTAL** | **~2500** | - |

---

## 🚀 Próximas Mejoras

### Funcionalidades Futuras
1. **Scanner QR Real** - Integrar zbarcam
2. **Mapa de EcoPuntos** - Geolocalización
3. **Backend** - API REST para sincronización
4. **Push Notifications** - Recordatorios de racha
5. **Compartir en Redes** - Social sharing

### Mejoras Técnicas
1. **SQLite** - Migrar cuando escale
2. **Caché** - Optimizar carga de datos
3. **Animaciones** - Transiciones fluidas
4. **Modo Offline** - Funcionar sin internet
5. **i18n** - Internacionalización

---

## 📝 Conclusión

El desarrollo de Reciclapp ha sido un **desafío técnico y educativo** que me permitió:

✅ Dominar Kivy/KivyMD  
✅ Implementar arquitecturas profesionales  
✅ Desarrollar sistemas de persistencia  
✅ Crear métricas propias para evaluación  
✅ Usar IA de forma responsable y eficiente  

**Los desafíos enfrentados y las soluciones encontradas son la verdadera evidencia de aprendizaje.**

---

**Autor:** Marcos Castro  
**Email:** mcastro2024@alu.uct.cl  
**Fecha:** Noviembre 2024
