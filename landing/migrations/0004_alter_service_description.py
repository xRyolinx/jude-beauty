# Generated by Django 4.2.4 on 2023-08-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]