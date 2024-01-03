# Generated by Django 4.2.5 on 2023-10-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0151_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='About Me'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, db_column='email', max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile_phone',
            field=models.CharField(blank=True, db_column='mobile_phone', max_length=15, null=True, unique=True, verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]