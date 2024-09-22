# Generated by Django 4.2.5 on 2024-01-07 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personplace',
            old_name='_priority',
            new_name='priority',
        ),
        migrations.RenameField(
            model_name='personplace',
            old_name='_responsibility',
            new_name='responsibility',
        ),
        migrations.RenameField(
            model_name='personplace',
            old_name='_role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_area',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_num_floors',
            new_name='num_floors',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_phoneNumber',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_postalcode',
            new_name='postalcode',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_statee',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='_usage',
            new_name='usage',
        ),
    ]
