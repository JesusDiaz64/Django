# Generated by Django 5.1.4 on 2025-01-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionContactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
