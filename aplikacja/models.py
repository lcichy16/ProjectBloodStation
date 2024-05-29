from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render,redirect


def validate_telefon(value):
    if not value.isdigit():
        raise ValidationError(("Numer telefonu może zawierać tylko cyfry."))


def validate_data_urodzenia(value):
    if value.year > 2005:
        raise ValidationError(("Osoba musi być pełnoletnia."))


class Dawca(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    data_urodzenia = models.DateField(validators=[validate_data_urodzenia])
    adres_mailowy = models.CharField(max_length=25)
    GRUPY_KRWI_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('0+', '0+'),
        ('0-', '0-'),
    ]
    grupa_krwi = models.CharField(max_length=3, choices=GRUPY_KRWI_CHOICES)
    numer_telefonu = models.CharField(max_length=20, validators=[validate_telefon])

    class Meta:
        verbose_name_plural = "Dawcy"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"



class Donacja(models.Model):
    dawca = models.ForeignKey(Dawca, on_delete=models.CASCADE)
    data_donacji = models.DateField()
    ilosc_krwi = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Donacje"

    def __str__(self):
        return f"Donacja {self.dawca} - {self.data_donacji}"


class Zamowienie(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    GRUPY_KRWI_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('0+', '0+'),
        ('0-', '0-'),
    ]
    grupa_krwi = models.CharField(max_length=3, choices=GRUPY_KRWI_CHOICES, default='A+')
    czynnik_Rh = models.CharField(max_length=1)
    data_zamowienia = models.DateField()
    ilosc_krwi = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Zamówienia"

    def __str__(self):
        return f"Zamówienie {self.id} - {self.uzytkownik.username}"


class Personel(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    stanowisko = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Personel"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Transfuzja(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    dawca = models.ForeignKey(Dawca, on_delete=models.CASCADE)
    data_transfuzji = models.DateTimeField()
    ilosc_przetransfuzowanej_krwi = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Transfuzje"

    def __str__(self):
        return f"Transfuzja {self.id} - {self.zamowienie.uzytkownik.username}"
