# Generated by Django 5.0.6 on 2024-07-01 12:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
