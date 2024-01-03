# Generated by Django 4.2.3 on 2023-08-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0005_alter_medicaldegree_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaldegree',
            name='category',
            field=models.CharField(choices=[('General', 'عمومی'), ('Specialty', 'تخصصی'), ('Subspecialty', 'فوق تخصصی'), ('Fellowship', 'فلوشیپ')], max_length=20, null=True, verbose_name='دسته\u200cبندی'),
        ),
    ]