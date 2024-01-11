# Generated by Django 4.2.5 on 2024-01-04 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialParameter',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='نام پارامتر مالی')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مقدار')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='زمان تراکنش')),
                ('category', models.CharField(max_length=100, verbose_name='دسته\u200cبندی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('product_name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ خرید')),
                ('quantity', models.IntegerField(verbose_name='تعداد')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت کل')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ پرداخت')),
                ('date', models.DateField(verbose_name='تاریخ پرداخت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ دریافت')),
                ('date', models.DateField(verbose_name='تاریخ دریافت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialTransaction',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='عنوان هزینه')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('_title', models.CharField(db_column='title', max_length=1966, null=True, verbose_name='Title')),
                ('_amount', models.CharField(db_column='amount', max_length=526, null=True, verbose_name='Amount')),
                ('_description', models.TextField(db_column='description', null=True, verbose_name='Description')),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Vat')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Discount')),
                ('invoice_number', models.CharField(max_length=50, null=True, verbose_name='Invoice Number')),
                ('document', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='نام بودجه')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ بودجه')),
                ('start_date', models.DateField(verbose_name='تاریخ شروع بودجه')),
                ('end_date', models.DateField(verbose_name='تاریخ پایان بودجه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ تنخواه')),
                ('date', models.DateField(verbose_name='تاریخ تنخواه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]