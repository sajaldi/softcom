# Generated by Django 5.1.3 on 2025-01-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
    ]
