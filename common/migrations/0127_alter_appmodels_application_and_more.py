# Generated by Django 4.2.5 on 2023-09-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0126_merge_20230921_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodels',
            name='application',
            field=models.CharField(choices=[('administration', 'administration'), ('food', 'food'), ('nursing', 'nursing'), ('shopping', 'shopping'), ('tourism', 'tourism'), ('accommodation', 'accommodation'), ('transportation', 'transportation'), ('treatment', 'treatment'), ('common', 'common'), ('communication', 'communication'), ('financialhub', 'financialhub')], max_length=50),
        ),
        migrations.RemoveField(
            model_name='settingmenus',
            name='tables',
        ),
        migrations.AlterUniqueTogether(
            name='appmodels',
            unique_together={('application', 'model')},
        ),
        migrations.RemoveField(
            model_name='appmodels',
            name='model',
        ),
        migrations.AddField(
            model_name='settingmenus',
            name='tables',
            field=models.ManyToManyField(blank=True, related_name='setting_menus', to='common.appmodels'),
        ),
    ]