# Generated by Django 4.2.3 on 2023-09-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0042_alter_settingmenus_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]