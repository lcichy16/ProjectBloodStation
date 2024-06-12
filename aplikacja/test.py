import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projekt.settings')
django.setup()

from projekt.models import Stacja

# Lista stacji do dodania
stacje = ['Gdańsk', 'Sopot', 'Gdynia']

# Dodaj stacje do bazy danych
for nazwa in stacje:
    Stacja.objects.get_or_create(nazwa=nazwa)
