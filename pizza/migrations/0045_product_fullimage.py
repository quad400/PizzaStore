# Generated by Django 4.1.4 on 2022-12-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0044_remove_settings_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fullimage',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
