# Generated by Django 4.1.7 on 2023-03-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0004_altkategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='altkategori',
            field=models.ManyToManyField(to='urunler.altkategori'),
        ),
    ]
