# Generated by Django 4.1.4 on 2022-12-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0015_alter_service_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='service',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
