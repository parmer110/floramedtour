# Generated by Django 4.2.3 on 2023-08-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_remove_systemsettingspic_max_image_file_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]