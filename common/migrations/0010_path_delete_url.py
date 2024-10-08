# Generated by Django 5.0.1 on 2024-01-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_alter_companywebsite_company'),
        ('common', '0009_alter_url_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('url', models.URLField(blank=True, verbose_name='Website Address')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
