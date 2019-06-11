# Generated by Django 2.1 on 2019-06-10 08:42

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('retailer_profile', '0002_auto_20190318_2136'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bouquet_id', models.CharField(max_length=120)),
                ('flower', models.CharField(max_length=120)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer_profile.Retailer')),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_id', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path)),
                ('size', models.DecimalField(decimal_places=1, default=1.0, max_digits=20)),
                ('flavour', models.CharField(max_length=100)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer_profile.Retailer')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
