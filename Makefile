# Definir comandos útiles para el proyecto

# Crear el entorno virtual
venv:
	python3 -m venv env

# Activar el entorno virtual
activate:
	source env/bin/activate

# Instalar dependencias
install:
	pip install -r requirements.txt

# Migrar la base de datos
migrate:
	python manage.py migrate

# Ejecutar el servidor de desarrollo
run:
	python manage.py runserver

# Ejecutar las pruebas
test:
	python manage.py test

# Limpiar archivos temporales y caché
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Inicialización completa del entorno
setup: venv install migrate
