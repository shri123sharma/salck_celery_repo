# Generated by Django 4.2 on 2023-04-05 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0011_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='City',
        ),
        migrations.RenameModel(
            old_name='Address',
            new_name='Country',
        ),
        migrations.RenameModel(
            old_name='Banking',
            new_name='State',
        ),
    ]