# Generated by Django 4.1.4 on 2022-12-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0023_aboutus_style_delay_aboutus_style_tabs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='active',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='show',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
