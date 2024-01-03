# Generated by Django 4.2.3 on 2023-09-10 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0054_person_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
    ]