# Generated by Django 4.1.4 on 2022-12-23 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0021_settings_logo_inverse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('sub_topic', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='about_us/')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='team/')),
            ],
        ),
        migrations.AddField(
            model_name='settings',
            name='image_about1',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
        migrations.AddField(
            model_name='settings',
            name='image_about2',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
        migrations.AddField(
            model_name='settings',
            name='image_background',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
        migrations.AddField(
            model_name='settings',
            name='image_home1',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='settings',
            name='image_home2',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='settings',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/'),
        ),
    ]
