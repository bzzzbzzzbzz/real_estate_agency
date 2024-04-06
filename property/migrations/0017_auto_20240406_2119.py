# Generated by Django 2.2.24 on 2024-04-06 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20240406_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Понравилось'),
        ),
    ]