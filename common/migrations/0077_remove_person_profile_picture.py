# Generated by Django 4.2.3 on 2023-09-11 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0076_alter_systemsettingspic_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='profile_picture',
        ),
    ]