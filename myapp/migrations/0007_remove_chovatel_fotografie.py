# Generated by Django 4.2 on 2023-06-17 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_chovatel_fotografie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chovatel',
            name='fotografie',
        ),
    ]
