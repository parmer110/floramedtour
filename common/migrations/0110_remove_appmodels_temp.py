# Generated by Django 4.2.5 on 2023-09-17 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0109_alter_appmodels_unique_together_appmodels_temp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appmodels',
            name='temp',
        ),
    ]