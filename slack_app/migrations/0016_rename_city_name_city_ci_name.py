# Generated by Django 4.2 on 2023-04-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0015_remove_country_country_name_city_city_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city_name',
            new_name='ci_name',
        ),
    ]
