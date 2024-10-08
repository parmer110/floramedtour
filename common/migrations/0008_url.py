# Generated by Django 5.0.1 on 2024-01-29 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_pictures_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('url', models.URLField(blank=True, null=True, verbose_name='Website Address')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='url', to='common.classification')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
