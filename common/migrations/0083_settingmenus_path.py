# Generated by Django 4.2.3 on 2023-09-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0082_systemsettingspic_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingmenus',
            name='path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]