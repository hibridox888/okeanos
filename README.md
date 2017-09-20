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
> - https://www.webfaction.com/
> - https://www.digitalocean.com

### Tech

* [Django == 1.11.4] - Framework web basado en Python
* [Materialize == 0.100.2] - Framework front-end con tendencia Material Design
* [Sass] - Para escribir codigo CSS más legible y rápido
* [Masonry]

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
