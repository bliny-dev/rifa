# Generated by Django 4.1.1 on 2023-05-28 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0003_alter_sorteio_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sorteio',
            name='premios',
        ),
        migrations.RemoveField(
            model_name='sorteio',
            name='promocaos',
        ),
        migrations.AddField(
            model_name='premios',
            name='Sorteio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sorteio.sorteio'),
        ),
        migrations.AddField(
            model_name='promocaos',
            name='Sorteio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sorteio.sorteio'),
        ),
        migrations.AlterField(
            model_name='sorteio',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]