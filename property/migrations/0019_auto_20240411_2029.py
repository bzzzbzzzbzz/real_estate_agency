# Generated by Django 2.2.24 on 2024-04-11 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20240410_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
    ]
