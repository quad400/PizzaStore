# Generated by Django 4.1.4 on 2022-12-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0019_settings_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]