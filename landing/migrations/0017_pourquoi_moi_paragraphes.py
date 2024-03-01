# Generated by Django 4.2.4 on 2023-08-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0016_about_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pourquoi_moi_Paragraphes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraphe', models.TextField()),
                ('order', models.IntegerField(unique=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pourquoi_paragraphes', to='landing.about')),
            ],
        ),
    ]