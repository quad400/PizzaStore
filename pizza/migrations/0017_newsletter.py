# Generated by Django 4.1.4 on 2022-12-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0016_alter_bookings_service_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]