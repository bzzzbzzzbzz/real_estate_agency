# Generated by Django 2.2.24 on 2024-03-22 19:16

from django.db import migrations

def change_type_of_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(change_type_of_building)
    ]
