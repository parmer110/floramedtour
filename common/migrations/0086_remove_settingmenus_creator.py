# Generated by Django 4.2.3 on 2023-09-14 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0085_settingmenus_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingmenus',
            name='creator',
        ),
    ]