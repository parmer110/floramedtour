# Generated by Django 4.1.5 on 2023-07-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_alter_person__firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='_address',
            field=models.TextField(db_column='address', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_birthdate',
            field=models.TextField(db_column='birthdate', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_lastname',
            field=models.TextField(db_column='lastname', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_mobile_phone',
            field=models.TextField(db_column='mobile_phone', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_national_code',
            field=models.TextField(db_column='national_code', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_passport_number',
            field=models.TextField(db_column='passport_number', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_sex',
            field=models.TextField(db_column='sex', null=True),
        ),
    ]