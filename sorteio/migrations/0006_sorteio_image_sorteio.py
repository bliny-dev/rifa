# Generated by Django 4.1.1 on 2023-05-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0005_remove_sorteio_images_sorteio_delete_images_sorteio'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorteio',
            name='image_sorteio',
            field=models.ImageField(default=True, upload_to='rifa_img/'),
            preserve_default=False,
        ),
    ]
