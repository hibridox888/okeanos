from django.conf.urls import url

from . import views

app_name = 'blogweb_blog'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detalle/(?P<slug>[\w-]+)/$', views.detail_entry, name='detail_entry'),
    url(r'^autor/(?P<username>[\w-]+)/$', views.list_author, name='list_author'),
    url(r'^etiqueta/(?P<title>[\w-]+)/$', views.list_tag, name='list_tag'),
]
