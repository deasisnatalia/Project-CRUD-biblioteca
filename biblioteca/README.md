DEPENDENCIAS
- Python 3.8+
- Django 4.0+
- Pillow


INSTALACION Y CONFIGURACION
1. Clonar el repositorio
  git clone https://github.com/deasisnatalia/Project-CRUD-biblioteca.git
  cd Project-CRUD-biblioteca

2. Crear entorno virtual
   python -m venv venv
   venv\Scripts\activate

3. Instalar dependencias
   pip intall django
   pip install pillow

4. Aplicar migraciones
   python manage.py makemigrations
   python manage.py migrate

5. Crear Superusuario
   python manage.py createsuperuser
   
6. Iniciar el servidor
   python manage.py runserver
