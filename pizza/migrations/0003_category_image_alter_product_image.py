# Generated by Django 4.1.4 on 2022-12-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_alter_product_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/'),
        ),
    ]
