# Generated by Django 5.1.3 on 2025-01-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmms', '0007_ordendetrabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='frecuencia',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]
