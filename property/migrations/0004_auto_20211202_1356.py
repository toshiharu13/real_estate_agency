# Generated by Django 2.2.24 on 2021-12-02 10:56

from django.db import migrations


def autofill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year > 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [migrations.RunPython(autofill_new_building_field)]


