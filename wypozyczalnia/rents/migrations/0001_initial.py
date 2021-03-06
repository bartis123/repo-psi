# Generated by Django 2.2.7 on 2019-11-21 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rezyser', models.CharField(max_length=200)),
                ('gatunek', models.CharField(max_length=200)),
                ('opis', models.CharField(max_length=500)),
                ('cena', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('telefon', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wypozyczenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataWypozyczenia', models.DateField()),
                ('dataZwrotu', models.DateField()),
                ('idFilm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rents.Film')),
                ('idKlient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rents.Klient')),
                ('idPracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rents.Pracownik')),
            ],
        ),
    ]
