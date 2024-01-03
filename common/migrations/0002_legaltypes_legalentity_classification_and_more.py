# Generated by Django 4.2.3 on 2023-08-17 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='legalentity',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='legal_entity', to='common.classification'),
        ),
        migrations.AlterField(
            model_name='legalentity',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legal_entity', to='common.legaltypes'),
        ),
    ]