# Generated by Django 4.2.3 on 2023-09-11 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_remove_companyaddressrole_company_and_more'),
        ('common', '0081_alter_person_email_alter_person_mobile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemsettingspic',
            name='company',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='system_settings_pic', to='administration.company'),
            preserve_default=False,
        ),
    ]