# Generated by Django 4.2 on 2023-06-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_chovatel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chovatel',
            name='foto',
            field=models.ImageField(blank=True, help_text='Zde můžete vložit fotografii vozu', null=True, upload_to='', verbose_name='Fotka vozu'),
        ),
    ]
