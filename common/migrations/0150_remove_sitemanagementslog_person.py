# Generated by Django 4.2.5 on 2023-10-15 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0149_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitemanagementslog',
            name='person',
        ),
    ]