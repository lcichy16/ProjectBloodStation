# Generated by Django 4.2.1 on 2023-06-10 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dawca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('data_urodzenia', models.DateField()),
                ('adres', models.CharField(max_length=100)),
                ('grupa_krwi', models.CharField(max_length=3)),
                ('czynnik_Rh', models.CharField(max_length=1)),
                ('numer_telefonu', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Dawcy',
            },
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('stanowisko', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Personel',
            },
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupa_krwi', models.CharField(max_length=3)),
                ('czynnik_Rh', models.CharField(max_length=1)),
                ('data_zamowienia', models.DateField()),
                ('ilosc_krwi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Zamowienia',
            },
        ),
        migrations.CreateModel(
            name='Transfuzja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_transfuzji', models.DateField()),
                ('ilosc_przetransfuzowanej_krwi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dawca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.dawca')),
                ('zamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.zamowienie')),
            ],
            options={
                'verbose_name_plural': 'Transfuzje',
            },
        ),
        migrations.CreateModel(
            name='Donacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_donacji', models.DateField()),
                ('ilosc_krwi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dawca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.dawca')),
            ],
            options={
                'verbose_name_plural': 'Donacje',
            },
        ),
    ]
