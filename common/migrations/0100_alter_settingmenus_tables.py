# Generated by Django 4.2.5 on 2023-09-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0099_settingmenus_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingmenus',
            name='tables',
            field=models.CharField(choices=[], max_length=50, null=True),
        ),
    ]