# Generated by Django 4.2.5 on 2023-10-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0141_alter_loginrecord_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginrecord',
            name='ip_validation_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]