# Generated by Django 4.1.4 on 2022-12-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0041_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]