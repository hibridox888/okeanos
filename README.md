# OKEANOS Project

![N|Solid](http://tucodigo.cl/static/img/check.jpg)

Esta aplicación es para OKEANOS, cumpliendo requisitos de:

  - Blog para entradas y proyectos
  - Traducciones español/inglés del sitio
  - El mismo formato que [Proaus]

# Para instalar:
- Instalar virtualenv y pip. O tambien se puede con easy_install
- Instalar librerias en el entorno virtual con:
```sh
(env)$ pip install -r requirements.txt
```
Ese archivo contiene todos los nombres de las librerías y versiones utilizadas para el proyecto
##### Recordar compilar el archivo SASS!
Se utilizó Koala (MacOs)

# Para archivos estaticos (fuera del sistema de administración):
```sh
(env)$ python manage.py collectstatic
```
# Para traducciones:
```sh
(env)$ django-admin.py makemessages -l en
(env)$ django-admin.py makemessages -l es
```
Luego ingresar a "/proyecto/locale/en/LC_MESSAGES/django.po" y agregar traducciones. Al finalizar compilar las traducciones con:
```sh
(env)$ python manage.py compilemessages
```


### TODO:
  - Imagenes reales de los miembros del equipo
  - Llenar de post
  
  
## Para modificar usuarios y sociales

ingresar a 'okeanos/templates/' y hay 2 archivos: 'equipo.html' y 'sociales.html'
- 'equipo.html': Es para cambiar las imagenes y redes sociales del equipo..
    - Agregar imagenes en directorio /okeanos/static/img/equipo/aquí
    - Luego hacer un 'python manage.py collectstatic' para agregar los cambios en producción de los archivos estaticos
- 'sociales.html': Son las redes sociales que aparecen en el footer de la web, al cambiarlas se cambiarán en toda la web

### Hosting recomendados:
> - [Webfaction]
> - [DigitalOcean]

### Tech

* [Django] - 1.11.4 - Framework web basado en Python
* [Sass] - Para escribir codigo CSS más legible y rápido
* [Masonry] - Acomodar Grids

   [Django]: <https://www.djangoproject.com/>
   [Sass]: <http://sass-lang.com/>
   [Masonry]: <https://masonry.desandro.com/>
   [Proaus]: <http://proaus.cl/>
   [OKEANOS]: <http://okeanos.tucodigo.cl/>
   [Webfaction]: <https://www.webfaction.com/>
   [DigitalOcean]: <https://www.digitalocean.com>
   [git-repo-url]: <https://github.com/user0able/okeanos.git>
   [node.js]: <http://nodejs.org>
   [jQuery]: <http://jquery.com>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
