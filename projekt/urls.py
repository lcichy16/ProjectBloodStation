from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import set_language
from aplikacja import views

admin.site.site_header = 'Admin panel'
admin.site.site_title = 'Admin panel'
admin.site.index_title = 'Admin panel'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.my_view, name='home'),
    path('i18n/setlang/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
    path('opinie/', views.opinie, name='opinie'),
    path('kontakt/', views.kontakt, name='kontakt'),
]
