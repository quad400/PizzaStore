# Generated by Django 4.1.4 on 2022-12-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0028_history_active_history_show_history_style_delay_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='style_delay',
        ),
        migrations.AlterField(
            model_name='settings',
            name='video',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
