# Generated by Django 4.2.4 on 2023-08-20 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_temoignage'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='About_Paragraphes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraphe', models.TextField()),
                ('order', models.IntegerField(unique=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphes', to='landing.about')),
            ],
        ),
    ]
