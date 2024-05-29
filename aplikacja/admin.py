from django.contrib import admin
from .models import Dawca, Donacja, Zamowienie, Personel, Transfuzja

admin.site.register(Dawca)
admin.site.register(Donacja)
admin.site.register(Zamowienie)
admin.site.register(Personel)
admin.site.register(Transfuzja)

