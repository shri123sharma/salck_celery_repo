# Generated by Django 4.2 on 2023-04-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0032_user_state_st_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='State',
            new_name='State_Model',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='city_model',
            name='city_pin_code',
        ),
    ]
