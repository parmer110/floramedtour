# Generated by Django 4.2.5 on 2023-09-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0127_alter_appmodels_application_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingmenus',
            name='tables',
        ),
        migrations.AddField(
            model_name='appmodels',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
    ]