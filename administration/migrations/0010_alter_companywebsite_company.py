# Generated by Django 5.0.1 on 2024-01-30 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_remove_companywebsite_url_companywebsite_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companywebsite',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_websites', to='administration.company'),
        ),
    ]