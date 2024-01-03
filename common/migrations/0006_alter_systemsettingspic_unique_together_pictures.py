# Generated by Django 4.2.3 on 2023-08-22 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_systemsettingspic_created_at_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='systemsettingspic',
            unique_together={('app', 'name')},
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('image', models.ImageField(blank=True, height_field='image_height', max_length=255, null=True, upload_to='images/', width_field='image_width')),
                ('image_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.systemsettingspic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]