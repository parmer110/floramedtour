# Generated by Django 4.2.3 on 2023-09-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0069_classification_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='app',
            field=models.CharField(blank=True, choices=[('administration', 'administration'), ('food', 'food'), ('nursing', 'nursing'), ('shopping', 'shopping'), ('tourism', 'tourism'), ('accommodation', 'accommodation'), ('transportation', 'transportation'), ('treatment', 'treatment'), ('common', 'common'), ('communication', 'communication'), ('financialhub', 'financialhub')], max_length=20, null=True, verbose_name='Application'),
        ),
    ]