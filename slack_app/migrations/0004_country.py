# Generated by Django 4.2 on 2023-04-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0003_city_company_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
