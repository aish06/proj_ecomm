# Generated by Django 2.1 on 2019-07-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_auto_20190701_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='cake_id',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
