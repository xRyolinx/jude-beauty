# Generated by Django 4.2.4 on 2023-08-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_about_pourquoi_moi_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_heure',
            field=models.CharField(default=' ', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rendez_vous',
            name='date_heure',
            field=models.CharField(default=' ', max_length=64),
            preserve_default=False,
        ),
    ]
