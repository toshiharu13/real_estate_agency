# Generated by Django 2.2.24 on 2021-12-03 11:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20211203_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_full_name', models.CharField(max_length=100, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=30, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца')),
                ('ownners_flats', models.ManyToManyField(related_name='flats_owners', to='property.Flat', verbose_name='квартиры в собственности')),
            ],
        ),
    ]
