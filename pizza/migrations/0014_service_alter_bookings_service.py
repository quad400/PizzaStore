# Generated by Django 4.1.4 on 2022-12-22 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0013_alter_bookings_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='bookings',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.service'),
        ),
    ]
