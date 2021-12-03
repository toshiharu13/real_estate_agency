# Generated by Django 2.2.24 on 2021-12-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='ownners_flats',
            field=models.ManyToManyField(blank=True, related_name='flats_owners', to='property.Flat', verbose_name='квартиры в собственности'),
        ),
    ]
