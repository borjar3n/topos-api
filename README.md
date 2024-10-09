# Topos API

Este proyecto implementa una API REST en Django para realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre "Topos". El objetivo del proyecto es permitir la gestión de información sobre topos y realizar diferentes tipos de pruebas (unitarias, de integración, funcionales, de seguridad y rendimiento) sobre la API.

## Tecnologías Utilizadas
- **Python 3.8+**
- **Django 3.2+**
- **Django REST Framework**
- **SQLite** (base de datos por defecto)

## Instalación

1. Clona el repositorio desde GitHub:
    ```bash
    git clone https://github.com/tu-usuario/topos-api.git
    cd topos-api
    ```

2. Crea un entorno virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `POST /api/topos/` - Crea un nuevo topo
- `GET /api/topos/` - Lista todos los topos
- `GET /api/topos/<id>/` - Detalla un topo específico
- `PUT /api/topos/<id>/` - Actualiza un topo específico
- `DELETE /api/topos/<id>/` - Elimina un topo específico

## Pruebas

Este proyecto incluye varios tipos de pruebas:

- **Unitarias**
- **De integración**
- **Funcionales**
- **De seguridad**
- **De rendimiento**

Para ejecutar todas las pruebas:
```bash
python manage.py test
