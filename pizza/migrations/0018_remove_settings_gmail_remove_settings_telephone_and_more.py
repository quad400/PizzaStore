# Generated by Django 4.1.4 on 2022-12-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0017_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='telephone',
        ),
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
