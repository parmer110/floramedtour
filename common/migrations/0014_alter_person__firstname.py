# Generated by Django 4.1.5 on 2023-07-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_alter_person__sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='_firstname',
            field=models.TextField(db_column='firstname', null=True),
        ),
    ]