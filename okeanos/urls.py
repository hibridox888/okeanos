"""okeanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

from settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from .views import home
from django.conf.urls import include, url

urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls), name='django-admin'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^$', home, name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog-app'), name='blog-index'),
    url(r'^enviado/$', TemplateView.as_view(template_name="web/enviado.html"), name='enviado'),
) + static(MEDIA_URL, document_root=MEDIA_ROOT)
