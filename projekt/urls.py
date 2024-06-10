"""
URL configuration for projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from aplikacja import views
from django.conf.urls.i18n import set_language

admin.site.site_header = 'Admin panel'  
admin.site.site_title = 'Admin panel'  
admin.site.index_title = 'Admin panel' 


urlpatterns = [
    path('', views.my_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('i18n/setlang/', set_language, name='set_language'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('admin/', admin.site.urls),
    path('opinie/', views.opinie, name='opinie'),
]

