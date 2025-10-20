# 🌱 Reciclapp

Aplicación móvil de reciclaje desarrollada con **KivyMD** y **Python**.

## 📱 Descripción

Reciclapp es una aplicación móvil que facilita el proceso de reciclaje, permitiendo a los usuarios:
- Iniciar sesión de forma segura
- Registrar materiales reciclables
- Ver estadísticas de reciclaje
- Gestionar su perfil de usuario

## 🛠️ Tecnologías

- **Frontend**: KivyMD (Material Design)
- **Backend**: Python
- **Base de datos**: MySQL
- **Arquitectura**: MVC (Model-View-Controller)

## 📁 Estructura del Proyecto

```
REPO/
├── app/                    # Código principal de la aplicación
│   ├── screens/            # Pantallas de la app
│   ├── components/         # Componentes reutilizables
│   ├── database/          # Gestión de base de datos
│   ├── auth/              # Autenticación
│   ├── styles/            # Estilos y temas
│   └── utils/             # Utilidades
├── assets/                # Recursos estáticos
│   ├── images/            # Imágenes
│   ├── icons/             # Iconos
│   └── sounds/            # Sonidos
├── config/                # Configuración
├── tests/                 # Pruebas unitarias
├── entorno/               # Entorno virtual
├── requirements.txt       # Dependencias
└── README.md             # Este archivo
```

## 🚀 Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd Reciclapp
   ```

2. **Activar el entorno virtual**:
   ```bash
   entorno\Scripts\Activate.ps1
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**:
   - Editar `config/database_config.py`
   - Configurar credenciales de MySQL

5. **Ejecutar la aplicación**:
   ```bash
   python app/main.py
   ```

## 📋 Dependencias

- kivy>=2.2.0
- kivymd>=1.2.0
- mysql-connector-python>=8.0.0
- Pillow>=9.0.0
- requests>=2.28.0
- python-dotenv>=0.19.0

## 🔧 Configuración

### Base de Datos
Edita el archivo `config/database_config.py` con tus credenciales de MySQL:

```python
DB_CONFIG = {
    'host': 'tu_servidor',
    'database': 'reciclapp_db',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'port': 3306
}
```

## 📱 Pantallas

- **Login**: Inicio de sesión de usuarios
- **Home**: Dashboard principal
- **Profile**: Perfil de usuario
- **Recycling**: Gestión de reciclaje
- **Stats**: Estadísticas de reciclaje

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Desarrollador

**MarcosC2119** - Desarrollado con ❤️ para promover el reciclaje y el cuidado del medio ambiente.
