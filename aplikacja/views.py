from django.shortcuts import render, redirect
from .models import Dawca, Opinia
from .forms import DawcaForm, OpiniaForm
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth import login

# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


from .models import Opinia

def opinie(request):
    if request.method == 'POST':
        form = OpiniaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opinie')  # Zmień 'opinie' na nazwę URL dla widoku opinii
    else:
        form = OpiniaForm()

    opinie_list = Opinia.objects.all()

    return render(request, 'opinie.html', {'form': form, 'opinie': opinie_list})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import KontaktForm

def kontakt(request):
    if request.method == 'POST':
        form = KontaktForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            send_mail(subject, message, from_email, ['your_email@example.com'])
            return redirect('kontakt')  # Możesz zmienić na stronę z podziękowaniem
    else:
        form = KontaktForm()

    return render(request, 'kontakt.html', {'form': form})


def my_view(request):
    dawcy_liczba = Dawca.objects.aggregate(liczba=Count('id'))
    context = {
        'dawcy_liczba': dawcy_liczba['liczba'],
    }
    return render(request, 'home.html', context)

def register_view(request):
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
from django.contrib.auth import login
from .forms import CustomUserForm, DawcaForm

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserForm, DawcaForm

from django.shortcuts import render, redirect
from .forms import CustomUserForm, DawcaForm


def register(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        dawca_form = DawcaForm(request.POST)
        if user_form.is_valid() and dawca_form.is_valid():
            user = user_form.save()
            dawca = dawca_form.save(commit=False)
            dawca.user = user
            dawca.save()
            return redirect('success_url')  # Zmień 'success_url' na właściwą nazwę URL
    else:
        user_form = CustomUserForm()
        dawca_form = DawcaForm()

    return render(request, 'register.html', {'user_form': user_form, 'dawca_form': dawca_form})


from django.shortcuts import render
from .forms import OpiniaForm

def dodaj_opinie(request):
    if request.method == 'POST':
        form = OpiniaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OpiniaForm()

    return render(request, 'dodaj_opinie.html', {'form': form})
