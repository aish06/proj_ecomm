# Generated by Django 2.1 on 2019-03-18 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contact',
            new_name='phone',
        ),
    ]
