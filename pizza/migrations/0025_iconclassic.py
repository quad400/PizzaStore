# Generated by Django 4.1.4 on 2022-12-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0024_aboutus_active_aboutus_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconClassic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('delay', models.CharField(max_length=2)),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
    ]
