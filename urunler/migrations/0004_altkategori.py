# Generated by Django 4.1.7 on 2023-03-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_kategori_urun_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
    ]
