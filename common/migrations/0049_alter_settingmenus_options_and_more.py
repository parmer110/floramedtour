# Generated by Django 4.2.3 on 2023-09-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0048_user_bio_user_created_at_user_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settingmenus',
            options={'ordering': ['cat', 'index', 'parent']},
        ),
        migrations.AlterUniqueTogether(
            name='settingmenus',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='settingmenus',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='common.settingmenus'),
        ),
        migrations.AlterUniqueTogether(
            name='settingmenus',
            unique_together={('cat', 'index', 'name', 'parent')},
        ),
        migrations.RemoveField(
            model_name='settingmenus',
            name='level',
        ),
    ]