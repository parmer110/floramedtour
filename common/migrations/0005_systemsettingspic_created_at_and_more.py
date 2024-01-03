# Generated by Django 4.2.3 on 2023-08-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_systemsettingspic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemsettingspic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='systemsettingspic',
            name='deleted_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='systemsettingspic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='systemsettingspic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]