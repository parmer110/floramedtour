# Generated by Django 4.2.3 on 2023-09-02 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_company_description_company_document_company_name'),
        ('treatment', '0060_alter_specialty_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='administration.company'),
        ),
    ]