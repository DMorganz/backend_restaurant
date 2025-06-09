# Aplicación de Restaurante

Este proyecto es una aplicación web completa para la gestión de un restaurante, con un backend en Django y un frontend en React.

## Backend (Django)

### Estructura del Proyecto

- **restaurant_backend/**: Configuración principal del proyecto Django
- **restaurant/**: Aplicación Django con los modelos, vistas y serializadores
- **media/**: Carpeta para almacenar imágenes subidas

### Modelos

1. **Categoría**:
   - nombre
   - descripción
   - imagen
   - activo
   - fecha_creación

2. **Plato**:
   - nombre
   - descripción
   - precio
   - imagen
   - categoría (clave foránea a Categoría)
   - disponible
   - destacado
   - fecha_creación

### API Endpoints

- **GET /**: Página de inicio con información de la API
- **GET /api/categorias/**: Lista de todas las categorías
- **POST /api/categorias/**: Crear una nueva categoría
- **GET /api/categorias/{id}/**: Detalles de una categoría específica
- **PUT /api/categorias/{id}/**: Actualizar una categoría
- **DELETE /api/categorias/{id}/**: Eliminar una categoría
- **GET /api/categorias/{id}/platos/**: Obtener platos de una categoría específica
- **GET /api/platos/**: Lista de todos los platos
- **POST /api/platos/**: Crear un nuevo plato
- **GET /api/platos/{id}/**: Detalles de un plato específico
- **PUT /api/platos/{id}/**: Actualizar un plato
- **DELETE /api/platos/{id}/**: Eliminar un plato
- **GET /api/platos/destacados/**: Obtener platos destacados
- **GET /api/platos/por_categoria/?categoria_id={id}**: Filtrar platos por categoría

## Instalación y Ejecución

### Requisitos

- Python 3.8+
- Django 5.2
- Django REST Framework
- Pillow (para manejo de imágenes)

### Configuración del Backend

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```
   python -m venv env
   ```
3. Activar el entorno virtual:
   - Windows: `env\Scripts\activate`
   - Linux/Mac: `source env/bin/activate`
4. Instalar dependencias:
   ```
   pip install django djangorestframework pillow django-cors-headers
   ```
5. Aplicar migraciones:
   ```
   python manage.py migrate
   ```
6. Crear superusuario:
   ```
   python manage.py createsuperuser
   ```
7. Ejecutar el servidor:
   ```
   python manage.py runserver
   ```

El backend estará disponible en http://127.0.0.1:8000/

## Frontend (React)

Para el frontend, se utilizará React con Axios para consumir la API y Tailwind CSS para el diseño. Se implementará en un proyecto separado.

## Despliegue

Para el despliegue se utilizará un servicio de hosting gratuito como:
- PythonAnywhere o Heroku para el backend
- Netlify o Vercel para el frontend 