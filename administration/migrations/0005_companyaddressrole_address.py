# Generated by Django 4.2.5 on 2024-01-04 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('administration', '0004_companyaddressrole_job_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyaddressrole',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_address_role', to='common.places'),
        ),
    ]
