# Generated by Django 4.2.4 on 2023-08-19 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='prix',
            field=models.CharField(max_length=64),
        ),
    ]