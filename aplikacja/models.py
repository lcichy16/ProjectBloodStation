from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value >= timezone.now().date():
        raise ValidationError("Data urodzenia musi być wcześniejsza niż bieżąca data.")

class CustomUser(AbstractUser):
    numer_telefonu = models.CharField(max_length=20, blank=True)
    grupa_krwi = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(validators=[validate_future_date], blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Dodanie related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Dodanie related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Dawca(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    grupa_krwi = models.CharField(max_length=10)
    adres_mailowy = models.EmailField()
    numer_telefonu = models.CharField(max_length=20)
    data_urodzenia = models.DateField(validators=[validate_future_date])

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Stacja(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Opinia(models.Model):
    stacja = models.ForeignKey(Stacja, on_delete=models.CASCADE)
    tresc = models.TextField()
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tresc

class Rejestracja(models.Model):
    dawca = models.ForeignKey(Dawca, on_delete=models.CASCADE)
    stacja = models.ForeignKey(Stacja, on_delete=models.CASCADE)
    data_rejestracji = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dawca} - {self.stacja}"
