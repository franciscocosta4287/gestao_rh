"""config_proct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    path('',              include('apps.core.urls')),
    path('emp/',     include('apps.empresas.urls')),
    path('func/', include('apps.funcionarios.urls')),
    path('doc/',    include('apps.documentos.urls')),
    path('dep/', include('apps.departamentos.urls')),
    path('he/',           include('apps.registro_hora_extra.urls')),
    path("admin/", admin.site.urls),
]
