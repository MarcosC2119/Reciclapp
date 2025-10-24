# 🧪 Tests para Reciclapp

Esta carpeta contiene todos los tests unitarios y de integración para la aplicación Reciclapp.

## 📂 Estructura

```
tests/
├── __init__.py              # Inicialización del paquete de tests
├── conftest.py              # Fixtures compartidas y configuración de pytest
├── test_main.py             # Tests para el módulo principal
├── test_screens.py          # Tests para las pantallas
└── README.md                # Este archivo
```

## 🚀 Ejecutar los tests

### Ejecutar todos los tests

```bash
pytest
```

### Ejecutar con cobertura

```bash
pytest --cov=app --cov-report=html
```

### Ejecutar tests específicos

```bash
# Solo tests unitarios
pytest -m unit

# Solo tests de integración
pytest -m integration

# Solo tests de UI
pytest -m ui

# Un archivo específico
pytest tests/test_screens.py

# Una clase específica
pytest tests/test_screens.py::TestLoginScreen

# Un test específico
pytest tests/test_screens.py::TestLoginScreen::test_toggle_password
```

### Modo verbose (más información)

```bash
pytest -v
```

### Modo silencioso

```bash
pytest -q
```

### Ver stdout/print statements

```bash
pytest -s
```

## 📊 Reportes de cobertura

Después de ejecutar los tests con cobertura, se generará un reporte HTML en:

```
htmlcov/index.html
```

Ábrelo en tu navegador para ver un análisis detallado de la cobertura de código.

## 🏷️ Marcadores (Markers)

Los tests están organizados con marcadores personalizados:

- `@pytest.mark.unit` - Tests unitarios para funciones y métodos individuales
- `@pytest.mark.integration` - Tests de integración entre componentes
- `@pytest.mark.ui` - Tests de interfaz de usuario
- `@pytest.mark.slow` - Tests que tardan más tiempo
- `@pytest.mark.skip_ci` - Tests que se saltean en CI/CD

## 🔧 Fixtures disponibles

### `app_config`
Configuración de la aplicación para tests
```python
def test_example(app_config):
    assert app_config["window_size"] == (360, 720)
```

### `mock_user_data`
Datos de usuario de ejemplo
```python
def test_user(mock_user_data):
    assert mock_user_data["name"] == "Ana Martínez"
```

### `mock_achievement_data`
Datos de logros de ejemplo
```python
def test_achievements(mock_achievement_data):
    assert len(mock_achievement_data) > 0
```

### `mock_community_post`
Post de comunidad de ejemplo
```python
def test_post(mock_community_post):
    assert mock_community_post["user"] == "Ana López"
```

## ✅ Buenas prácticas

1. **Nombra los tests de forma descriptiva**: `test_toggle_password_changes_visibility`
2. **Un assert por test** (cuando sea posible)
3. **Usa fixtures** para datos de prueba reutilizables
4. **Mock dependencias externas** (API calls, file I/O, etc.)
5. **Tests independientes**: cada test debe poder ejecutarse solo
6. **Documenta tests complejos** con docstrings

## 📝 Ejemplo de test

```python
import pytest
from unittest.mock import Mock

class TestMyScreen:
    """Tests para MyScreen"""
    
    @pytest.mark.unit
    def test_navigation(self):
        """Verifica que la navegación funciona correctamente"""
        from app.screens.my_screen import MyScreen
        
        screen = MyScreen()
        screen.manager = Mock()
        
        screen.go_home()
        
        assert screen.manager.current == 'home'
```

## 🐛 Debugging tests

Para debuggear un test específico:

```bash
pytest tests/test_screens.py::TestLoginScreen::test_toggle_password -vv -s
```

O usando breakpoint en el código:

```python
def test_something():
    x = calculate_something()
    breakpoint()  # El debugger se detendrá aquí
    assert x == expected
```

## 📈 Objetivo de cobertura

El objetivo es mantener una cobertura de código de **al menos 80%** en el proyecto.

Áreas críticas deben tener **90%+** de cobertura:
- Lógica de negocio
- Validaciones
- Cálculos de impacto ambiental
- Gestión de usuarios

## 🔄 Integración Continua

Los tests se ejecutan automáticamente en cada:
- Push a la rama main
- Pull Request
- Antes de cada merge

Todos los tests deben pasar antes de hacer merge.

