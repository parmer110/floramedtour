# Generated by Django 4.2.5 on 2023-10-15 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0140_loginrecord_device_type_loginrecord_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrecord',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='login_record', to='common.location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_session', to='common.location', verbose_name='Location'),
        ),
    ]