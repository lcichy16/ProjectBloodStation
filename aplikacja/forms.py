from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Dawca, Opinia

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Wymagane. Podaj prawidłowy adres email.')

    class Meta:
        model = AbstractUser
        fields = ['email', 'password1', 'password2']


class DawcaForm(forms.ModelForm):
    class Meta:
        model = Dawca
        fields = ['imie', 'nazwisko', 'grupa_krwi', 'adres_mailowy', 'numer_telefonu', 'data_urodzenia']

class OpiniaForm(forms.ModelForm):
    class Meta:
        model = Opinia
        fields = ['stacja', 'tresc']


from django import forms

class KontaktForm(forms.Form):
    name = forms.CharField(max_length=100, label='Twoje imię')
    email = forms.EmailField(label='Twój email')
    subject = forms.CharField(max_length=100, label='Temat')
    message = forms.CharField(widget=forms.Textarea, label='Wiadomość')


