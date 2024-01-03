# Generated by Django 4.2.3 on 2023-08-27 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_remove_user_group_delete_groupsuser'),
        ('treatment', '0039_buccalfatremovaldiagnosis_buccalfatremovalpatient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadLiftDiagnosis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThreadLiftPatient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='threadlift_patient', to='common.person')),
            ],
            options={
                'db_table': 'threadlift_patient',
            },
        ),
        migrations.CreateModel(
            name='ThreadLiftPrescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('medication', models.CharField(max_length=100, verbose_name='نام دارو')),
                ('dosage', models.CharField(max_length=50, verbose_name='مقدار دوز دارو')),
                ('usage_instructions', models.TextField(verbose_name='دستورات مصرف دارو')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThreadLiftSymptom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='نام علامت')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='buccalfatremovalprocedure',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='buccalfatremovalprocedure',
            name='deleted_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='buccalfatremovalprocedure',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='buccalfatremovalprocedure',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ThreadLiftTreatment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('treatment_date', models.DateTimeField(verbose_name='تاریخ درمان')),
                ('diagnosis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='treatment.threadliftdiagnosis', verbose_name='تشخیص')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.threadliftpatient', verbose_name='بیمار')),
                ('prescriptions', models.ManyToManyField(blank=True, to='treatment.threadliftprescription', verbose_name='نسخه\u200cهای دارویی')),
                ('symptoms', models.ManyToManyField(blank=True, to='treatment.threadliftsymptom', verbose_name='علائم')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThreadLiftProcedure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('procedure_date', models.DateTimeField(verbose_name='تاریخ مرحله درمانی')),
                ('procedure_description', models.TextField(verbose_name='توضیحات مرحله درمانی')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='treatment.threadlifttreatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThreadLiftPostTreatment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('post_treatment_notes', models.TextField(verbose_name='یادداشت\u200cهای پس از درمان')),
                ('follow_up_date', models.DateTimeField(verbose_name='تاریخ پیگیری بعدی')),
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post_treatment', to='treatment.threadlifttreatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='threadliftdiagnosis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.threadliftpatient', verbose_name='بیمار'),
        ),
        migrations.AddField(
            model_name='threadliftdiagnosis',
            name='symptoms',
            field=models.ManyToManyField(blank=True, to='treatment.threadliftsymptom', verbose_name='علائم'),
        ),
    ]