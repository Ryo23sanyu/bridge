# Generated by Django 4.2.7 on 2023-11-22 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_product_picture_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]