# 📱 Guía Rápida: Cómo Crear Nuevas Pantallas

## 🎯 Concepto Clave

Cada pantalla tiene **DOS archivos**:
1. **`.py`** → Lógica (métodos, funciones, datos)
2. **`.kv`** → Diseño (interfaz visual, layout, estilos)

## 🚀 Pasos para Crear una Nueva Pantalla

### 1️⃣ Crea el archivo Python

**Archivo**: `app/screens/mi_pantalla_screen.py`

```python
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Cargar el diseño KV
Builder.load_file('app/screens/mi_pantalla_screen.kv')

class MiPantallaScreen(MDScreen):
    """Descripción de tu pantalla"""
    
    def mi_funcion(self):
        """Tu lógica aquí"""
        print("Ejecutando lógica")
```

### 2️⃣ Crea el archivo KV

**Archivo**: `app/screens/mi_pantalla_screen.kv`

```kv
#:kivy 2.3.1

<MiPantallaScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Mi Pantalla"
        
        MDLabel:
            text: "Contenido aquí"
            halign: "center"
```

### 3️⃣ Registra la pantalla

**En** `app/screens/__init__.py`:

```python
from app.screens.mi_pantalla_screen import MiPantallaScreen

__all__ = ['HomeScreen', 'ProfileScreen', 'MiPantallaScreen']
```

### 4️⃣ Añade al ScreenManager

**En** `app/main.kv`:

```kv
#:import MiPantallaScreen app.screens.mi_pantalla_screen

ScreenManager:
    MiPantallaScreen:
        name: 'mi_pantalla'
```

### 5️⃣ Navega a tu pantalla

**Desde Python**:
```python
self.manager.current = 'mi_pantalla'
```

**Desde KV**:
```kv
MDRaisedButton:
    on_release: app.root.current = 'mi_pantalla'
```

## ✨ Ejemplos Útiles

### Botón que ejecuta una función
```kv
MDRaisedButton:
    text: "Click Me"
    on_release: root.mi_funcion()
```

### Lista de items
```kv
ScrollView:
    MDList:
        OneLineListItem:
            text: "Item 1"
        OneLineListItem:
            text: "Item 2"
```

### Card con contenido
```kv
MDCard:
    padding: dp(20)
    spacing: dp(10)
    orientation: 'vertical'
    
    MDLabel:
        text: "Título"
        font_style: "H6"
    
    MDLabel:
        text: "Descripción"
```

## 🔧 Tips

- **Nombres**: Usa `snake_case` para archivos, `PascalCase` para clases
- **Consistencia**: `nombre_screen.py` + `nombre_screen.kv` + `NombreScreen`
- **Testing**: Prueba cada pantalla antes de añadir más
- **Templates**: Usa los archivos `TEMPLATE_screen.*` como base

## 📚 Componentes Comunes

| Componente | Uso |
|------------|-----|
| `MDBoxLayout` | Organizar elementos vertical/horizontal |
| `MDLabel` | Mostrar texto |
| `MDRaisedButton` | Botones |
| `MDCard` | Tarjetas Material Design |
| `MDTopAppBar` | Barra superior |
| `MDTextField` | Campos de texto |
| `MDIcon` | Iconos |
| `ScrollView` | Áreas desplazables |

## 🎨 Propiedades Útiles en KV

```kv
# Tamaños
size_hint: 0.5, 0.5      # 50% ancho y alto
size_hint_x: 0.8         # 80% ancho
height: dp(100)          # 100 píxeles de densidad

# Posición
pos_hint: {"center_x": 0.5, "center_y": 0.5}  # Centrado

# Espaciado y padding
padding: dp(20)          # Espacio interno
spacing: dp(10)          # Espacio entre widgets

# Colores
md_bg_color: app.theme_cls.primary_color
theme_text_color: "Primary"

# Alineación
halign: "center"         # Horizontal
valign: "center"         # Vertical
```

¡Ya estás listo para crear pantallas! 🎉

