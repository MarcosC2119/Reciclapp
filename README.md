# Proyecto KivyMD

Proyecto base para desarrollo de aplicaciones con KivyMD en Python, con separación de diseño (.kv) y lógica (.py).

## 📁 Estructura del Proyecto

```
REPO/
├── app/
│   ├── __init__.py
│   ├── main.py                      # Aplicación principal
│   ├── main.kv                      # Diseño principal y ScreenManager
│   ├── screens/                     # Pantallas de la aplicación
│   │   ├── __init__.py
│   │   ├── home_screen.py          # Lógica de pantalla de inicio
│   │   ├── home_screen.kv          # Diseño de pantalla de inicio
│   │   ├── profile_screen.py       # Lógica de pantalla de perfil
│   │   ├── profile_screen.kv       # Diseño de pantalla de perfil
│   │   ├── TEMPLATE_screen.py.example    # Template para nuevas pantallas
│   │   └── TEMPLATE_screen.kv.example    # Template para diseños
│   ├── components/                  # Componentes reutilizables
│   │   └── __init__.py
│   └── assets/                      # Recursos (imágenes, iconos, etc.)
│       ├── images/
│       └── icons/
├── entorno/                         # Entorno virtual de Python
├── requirements.txt                 # Dependencias del proyecto
├── .gitignore
├── LICENSE
└── README.md
```

## 🎨 Arquitectura: Separación de Diseño y Lógica

Este proyecto sigue el patrón de **separación de responsabilidades**:

- **Archivos `.py`**: Contienen la lógica de negocio, métodos y funcionalidad
- **Archivos `.kv`**: Contienen el diseño visual, layout y estilos

### Ventajas de esta arquitectura:
- ✅ Código más limpio y organizado
- ✅ Fácil mantenimiento
- ✅ Diseñadores pueden trabajar en .kv sin tocar Python
- ✅ Reutilización de componentes
- ✅ Testing más sencillo

## 🚀 Instalación

### 1. Activar el entorno virtual

   ```bash
# Windows
.\entorno\Scripts\activate

# Linux/Mac
source entorno/bin/activate
```

### 2. Instalar dependencias (si es necesario)

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecutar la Aplicación

   ```bash
   python app/main.py
   ```

## 📝 Cómo Crear una Nueva Pantalla

### Opción 1: Usar los templates

1. Copia los archivos template:
   ```bash
   # Copia el archivo Python
   cp app/screens/TEMPLATE_screen.py.example app/screens/mi_pantalla_screen.py
   
   # Copia el archivo KV
   cp app/screens/TEMPLATE_screen.kv.example app/screens/mi_pantalla_screen.kv
   ```

2. Edita `mi_pantalla_screen.py`:
   - Reemplaza `TEMPLATE` con el nombre de tu pantalla
   - Actualiza el nombre del archivo .kv a cargar
   - Implementa tu lógica

3. Edita `mi_pantalla_screen.kv`:
   - Reemplaza `<TEMPLATEScreen>` con `<MiPantallaScreen>`
   - Diseña tu interfaz

4. Registra la pantalla en `app/screens/__init__.py`:
   ```python
   from app.screens.mi_pantalla_screen import MiPantallaScreen
   
   __all__ = ['HomeScreen', 'ProfileScreen', 'MiPantallaScreen']
   ```

5. Añade la pantalla al ScreenManager en `app/main.kv`:
   ```kv
   #:import MiPantallaScreen app.screens.mi_pantalla_screen
   
   ScreenManager:
       MiPantallaScreen:
           name: 'mi_pantalla'
   ```

### Opción 2: Desde cero

**Archivo Python** (`app/screens/ejemplo_screen.py`):
```python
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file('app/screens/ejemplo_screen.kv')

class EjemploScreen(MDScreen):
    def mi_metodo(self):
        print("Hola desde EjemploScreen")
```

**Archivo KV** (`app/screens/ejemplo_screen.kv`):
```kv
#:kivy 2.3.1

<EjemploScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        
        MDLabel:
            text: "Mi Pantalla"
            halign: "center"
```

## 🎯 Navegación entre Pantallas

En el archivo `.py`:
```python
# Navegar a otra pantalla
self.manager.current = 'nombre_pantalla'
```

En el archivo `.kv`:
```kv
MDRaisedButton:
    text: "Ir a Perfil"
    on_release: app.root.current = 'profile'
```

## 🎨 Componentes Principales de KivyMD

- `MDScreen`: Pantalla base
- `MDBoxLayout`: Layout en caja (vertical/horizontal)
- `MDLabel`: Texto
- `MDRaisedButton`: Botón elevado
- `MDCard`: Tarjeta Material Design
- `MDTopAppBar`: Barra superior
- `MDIcon`: Iconos Material Design
- `ScrollView`: Área desplazable

## 📚 Recursos

- [Documentación KivyMD](https://kivymd.readthedocs.io/)
- [Galería de Componentes KivyMD](https://kivymd.readthedocs.io/en/latest/components/)
- [Lenguaje Kivy (.kv)](https://kivy.org/doc/stable/guide/lang.html)

## 🛠️ Tecnologías

- **Python 3.12**
- **Kivy 2.3.1** - Framework para desarrollo de aplicaciones
- **KivyMD 1.2.0** - Componentes Material Design para Kivy

## 📄 Licencia

Ver archivo LICENSE para más detalles.
