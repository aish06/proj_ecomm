# Generated by Django 2.1 on 2019-06-19 14:46

import cake.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cake.models.upload_image_path),
        ),
    ]
