# Generated by Django 4.2.3 on 2023-09-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_remove_user_group_delete_groupsuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='translate',
            name='french',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translate',
            name='german',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translate',
            name='italian',
            field=models.TextField(blank=True, null=True),
        ),
    ]