from django.conf.urls import url

from . import views

app_name = 'blogweb_blog'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detalle/(?P<slug>[\w-]+)/$', views.detail_entry, name='detail_entry'),
]
