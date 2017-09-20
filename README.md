# OKEANOS Project

![N|Solid](http://tucodigo.cl/static/img/check.jpg)

Esta aplicación es para OKEANOS, cumpliendo requisitos de:

  - Blog para entradas y proyectos
  - Traducciones español/inglés del sitio
  - El mismo formato que http://proaus.cl/

# Para instalar:
- Instalar virtualenv y pip. O tambien se puede con easy_install
- Instalar librerias en el entorno virtual con:
```sh
(env)$ pip install -r requirements.txt
```
Ese archivo contiene todos los nombres de las librerías y versiones utilizadas para el proyecto
##### Recordar compilar el archivo SASS!
Se utilizó Koala (MacOs)
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
   [Webfaction]: <https://www.webfaction.com/>
   [DigitalOcean]: <https://www.digitalocean.com>
   [git-repo-url]: <https://github.com/user0able/okeanos.git>
   [node.js]: <http://nodejs.org>
   [jQuery]: <http://jquery.com>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
