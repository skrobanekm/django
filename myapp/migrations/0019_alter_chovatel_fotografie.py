# Generated by Django 4.2 on 2023-06-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_chovatel_fotografie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chovatel',
            name='fotografie',
            field=models.ImageField(blank=True, null=True, upload_to='chovatele', verbose_name='Fotografie'),
        ),
    ]
