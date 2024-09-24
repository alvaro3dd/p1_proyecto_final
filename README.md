# CodeHouse 

## Autor

Alvaro Cancino 

[Linkedin](https://www.linkedin.com/in/alvarocancino/)
[Github](https://github.com/alvaro3dd)

## Proyecto - Links

Pythonanywhere: https://alvaro3d.pythonanywhere.com
Video explicación del proyecto: https://www.youtube.com/watch?v=lRacTrE1EYo

## Nombre de la Aplicación
Giga Computers


## Descripción
Giga Computers es una tienda en línea especializada en la venta de elementos de computación. Ofrece una amplia gama de productos, desde componentes de PC y accesorios, hasta equipos completos y soluciones tecnológicas para profesionales y gamers.


# **Instalación**
Primera parte proyecto final "CodeHouse"

1. Clonar el repositorio desde Github:
Link: https://github.com/alvaro3dd/p1_proyecto_final.git

    git clone NombreRepositorio

    Acceder al repositorio:

        cd NombreRepositorio

    Abrir  Visual Studio Code (VSCode) en la carpeta esta carpeta:

        code .

2. Crear y Activar un entorno virtual:

    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate

3. Instalar dependencias:

   - pip install django

4. Realizar las migraciones:

    - python manage.py migrate

5. Crear un superusuario para acceder al panel de administración de Django:

    - python manage.py createsuperuser

6. Iniciar el servidor:
    - python manage.py runserver


# **Orden de Prueba**

1. Pagina Principal
    - URL: http://127.0.0.1:8000
    - Descripción: Pagina de inicio que hereda estructura HTML de base.html en la app CORE.
    Acá puede encontra accesos a Home y el unica App visible "Productos"

2. App Productos:
    - URL: http://127.0.0.1:8000/products/
    - Descripción: En la App Productos puede encontrar los 3 modelos de la web (Productos, Categorias y Marcas).

3. Modelo Productos:
     - URL: http://127.0.0.1:8000/products/product/list
     - Descripción: Puede contrar el listado actual de productos del Data Base (SQLite), junto con las siguiente funcionalidades:
        * Crear Registro: Acceder al form para crear nuevos productos.
        * Buscar: Permite realizar una busqueda sobre la lista de objetos
        * Detalle, modificar y borrar son views agreegadas para mayor funcionalidad a la hora de modificar el stock actual de productos.

4. Modelo Categorias:
     - URL: http://127.0.0.1:8000/products/product/list
     - Descripción: Puede contrar el listado actual de categorias del Data Base (SQLite), junto con las siguiente funcionalidades:
        * Crear Registro: Acceder al form para crear nuevas categorias.
        * Buscar: Permite realizar una busqueda sobre la lista de categorias


5. Modelo Marcas:
     - URL: http://127.0.0.1:8000/products/brand/list
     - Descripción: Puede contrar el listado actual de marcas del Data Base (SQLite), junto con las siguiente funcionalidades:
        * Crear Registro: Acceder al form para crear nuevas marcas.
        * Buscar: Permite realizar una busqueda sobre la lista de maracs


# **Funcionalidades Principales**


1. Herencia de HTML:

    Archivo base: templates/core/base.html
    Ejemplo de uso: templates/product/index.html, templates/product/list.html,  templates/product/form.html.

2. Modelos:
    Ubicación: product/models.py

    Clases:
    Clase Category : Junta los productos en categorias como: Pantallas, Teclados etc...
    Clase Brand: Representa la marca de cada equipo de computación
    Clase Product: Crea la estructura de los productos de computación con variables de clase nombre, descripción, precio, stock, especificaiones y heredando brand y categoria

3. Formularios:
    Ubicación: product/forms.py
    Formularios para: Category, Brand, Product.
   
4. Vistas:

    Ubicación: app_name/views.py
    Controladores para las rutas principales: insertar, buscar, etc

Notas adicionales
Asegúrate de haber configurado las variables de entorno si es necesario.
Si encuentras algún problema, revisa los logs en la consola para más detalles. .

