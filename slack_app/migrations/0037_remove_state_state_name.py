# Generated by Django 4.2 on 2023-04-05 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0036_city_model_city_pin_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='state_name',
        ),
    ]