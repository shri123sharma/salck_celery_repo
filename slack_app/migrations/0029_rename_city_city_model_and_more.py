# Generated by Django 4.2 on 2023-04-05 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0028_rename_coun_country_rename_st_name_state_state_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='City_Model',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='coun_name',
            new_name='country_name',
        ),
    ]
