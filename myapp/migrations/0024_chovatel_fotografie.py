# Generated by Django 4.2 on 2023-06-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_remove_zvire_fotografie'),
    ]

    operations = [
        migrations.AddField(
            model_name='chovatel',
            name='fotografie',
            field=models.ImageField(blank=True, null=True, upload_to='chovatel', verbose_name='Fotografie'),
        ),
    ]
