"""Minimarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title = "API de gestion de minimarket",
        default_version = "v1",
        description = "API usando DRF para el manejo de un minimarket con varios almacenes",
        terms_of_service = "https://www.google.com",
        contact = openapi.Contact(email="ederiveroman@gmail.com"),
        # https://es.wikipedia.org/wiki/Licencia_de_software
        license = openapi.License(name="MIT", url="https://es.wikipedia.org/wiki/Licencia_MIT")
    ),
    public = True,
    permission_classes = ( permissions.AllowAny, ),
)


urlpatterns = [
    path('',schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('minimarket/', include('administracion.urls')),
]
