# Generated by Django 4.1.1 on 2023-05-28 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0006_sorteio_image_sorteio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premios',
            name='Sorteio',
        ),
        migrations.AddField(
            model_name='sorteio',
            name='premio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sorteio.premios'),
        ),
    ]
