from django import forms
from .models import Dawca

class DawcaForm(forms.ModelForm):
    class Meta:
        model = Dawca
        fields = ['imie', 'nazwisko', 'data_urodzenia', 'adres_mailowy', 'numer_telefonu','grupa_krwi']



from django import forms
from .models import Opinia

class OpiniaForm(forms.ModelForm):
    class Meta:
        model = Opinia
        fields = ['stacja', 'tresc']