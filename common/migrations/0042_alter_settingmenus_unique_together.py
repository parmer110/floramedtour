# Generated by Django 4.2.3 on 2023-09-07 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_company_description_company_document_company_name'),
        ('common', '0041_settingmenus_company'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='settingmenus',
            unique_together={('application', 'page_name', 'index', 'level', 'company')},
        ),
    ]