from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Dawca
from .forms import DawcaForm


def opinie(request):
    return render(request, 'opinie.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def my_view(request):
    dawcy_liczba = Dawca.objects.aggregate(liczba=Count('id'))

    context = {
        'dawcy_liczba': dawcy_liczba['liczba'],
    }

    return render(request, 'home.html', context)

def register_view(request):
    form = DawcaForm()
    return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = DawcaForm(request.POST)
        if form.is_valid():
            dawca = form.save(commit=False)
            grupa_krwi = request.POST.get('grupa_krwi')
            dawca.grupa_krwi = grupa_krwi
            dawca.save()
            return render(request, 'success_page.html')
    else:
        form = DawcaForm()
    
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import OpiniaForm

from django.shortcuts import render
from .models import Opinia

def opinie(request):
    opinie = Opinia.objects.all()
    return render(request, 'opinie.html', {'opinie': opinie})


def dodaj_opinie(request):
    if request.method == 'POST':
        form = OpiniaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opinie')
    else:
        form = OpiniaForm()
    return render(request, 'dodaj_opinie.html', {'form': form})

