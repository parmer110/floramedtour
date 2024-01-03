# Generated by Django 4.2.5 on 2023-09-14 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common', '0095_auditlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='ipv4_address',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='ipv6_address',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv6'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='action',
            field=models.CharField(max_length=10),
        ),
    ]