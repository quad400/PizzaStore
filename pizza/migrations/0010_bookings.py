# Generated by Django 4.1.4 on 2022-12-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0009_gallery_height_gallery_width'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('service', models.CharField(choices=[('Party', 'Party'), ('Dine-In', 'Dine-In'), ('Carry-Out', 'Carry-Out'), ('Event Catering', 'Event Catering')], default='Party', max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]