# Generated by Django 5.0.1 on 2024-01-28 23:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_appmodels_application_alter_classification_app_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture', to=settings.AUTH_USER_MODEL),
        ),
    ]
