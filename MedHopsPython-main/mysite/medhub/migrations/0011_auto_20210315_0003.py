# Generated by Django 3.1.7 on 2021-03-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medhub', '0010_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='product',
            name='mrp',
            field=models.IntegerField(default=200),
        ),
    ]
