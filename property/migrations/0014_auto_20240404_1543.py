# Generated by Django 2.2.24 on 2024-04-04 12:43

from django.db import migrations

def move_data_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            owner_name=flat.owner,
            owner_number=flat.owners_phonenumber,
            owner_pure_number=flat.owner_pure_phone
        )

        if created:
            owner.owner_flat.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner'),
    ]

    operations = [
        migrations.RunPython(move_data_to_owner),
    ]
