# Generated by Django 4.2.5 on 2023-12-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0183_remove_settingmenus_individual_permission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingmenus',
            name='individual_permission',
            field=models.ManyToManyField(blank=True, related_name='setting_menus', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='settingmenus',
            name='tables',
            field=models.ManyToManyField(blank=True, related_name='setting_menus', to='contenttypes.contenttype'),
        ),
    ]