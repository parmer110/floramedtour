# Generated by Django 4.2.5 on 2023-12-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0169_remove_user_created_at_remove_user_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodels',
            name='application',
            field=models.CharField(choices=[('administration', 'administration'), ('food', 'food'), ('nursing', 'nursing'), ('shopping', 'shopping'), ('tourism', 'tourism'), ('accommodation', 'accommodation'), ('transportation', 'transportation'), ('treatment', 'treatment'), ('common', 'common'), ('communication', 'communication'), ('financialhub', 'financialhub'), ('softdelete', 'softdelete'), ('rest_framework', 'rest_framework'), ('rest_framework_simplejwt', 'rest_framework_simplejwt'), ('sslserver', 'sslserver'), ('corsheaders', 'corsheaders'), ('rest_framework_simplejwt.token_blacklist', 'rest_framework_simplejwt.token_blacklist')], max_length=50),
        ),
        migrations.AlterField(
            model_name='classification',
            name='app',
            field=models.CharField(blank=True, choices=[('administration', 'administration'), ('food', 'food'), ('nursing', 'nursing'), ('shopping', 'shopping'), ('tourism', 'tourism'), ('accommodation', 'accommodation'), ('transportation', 'transportation'), ('treatment', 'treatment'), ('common', 'common'), ('communication', 'communication'), ('financialhub', 'financialhub'), ('softdelete', 'softdelete'), ('rest_framework', 'rest_framework'), ('rest_framework_simplejwt', 'rest_framework_simplejwt'), ('sslserver', 'sslserver'), ('corsheaders', 'corsheaders'), ('rest_framework_simplejwt.token_blacklist', 'rest_framework_simplejwt.token_blacklist')], max_length=50, null=True, verbose_name='Application'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='application',
            field=models.CharField(choices=[('administration', 'administration'), ('food', 'food'), ('nursing', 'nursing'), ('shopping', 'shopping'), ('tourism', 'tourism'), ('accommodation', 'accommodation'), ('transportation', 'transportation'), ('treatment', 'treatment'), ('common', 'common'), ('communication', 'communication'), ('financialhub', 'financialhub'), ('softdelete', 'softdelete'), ('rest_framework', 'rest_framework'), ('rest_framework_simplejwt', 'rest_framework_simplejwt'), ('sslserver', 'sslserver'), ('corsheaders', 'corsheaders'), ('rest_framework_simplejwt.token_blacklist', 'rest_framework_simplejwt.token_blacklist')], max_length=50),
        ),
        migrations.AlterField(
            model_name='systemsettingspic',
            name='app',
            field=models.CharField(blank=True, choices=[('administration', 'administration'), ('food', 'food'), ('nursing', 'nursing'), ('shopping', 'shopping'), ('tourism', 'tourism'), ('accommodation', 'accommodation'), ('transportation', 'transportation'), ('treatment', 'treatment'), ('common', 'common'), ('communication', 'communication'), ('financialhub', 'financialhub'), ('softdelete', 'softdelete'), ('rest_framework', 'rest_framework'), ('rest_framework_simplejwt', 'rest_framework_simplejwt'), ('sslserver', 'sslserver'), ('corsheaders', 'corsheaders'), ('rest_framework_simplejwt.token_blacklist', 'rest_framework_simplejwt.token_blacklist')], max_length=50, null=True),
        ),
    ]