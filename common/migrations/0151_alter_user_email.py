# Generated by Django 4.2.5 on 2023-10-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0150_remove_sitemanagementslog_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]