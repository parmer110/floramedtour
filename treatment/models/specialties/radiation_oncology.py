from django.db import models

name = "Radiation Oncology"

class Patient(models.Model):
    # فیلدهای مربوط به بیمار
    full_name = models.CharField(max_length=100, verbose_name='نام کامل بیمار')
    age = models.PositiveIntegerField(verbose_name='سن')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.full_name

class RadiationProcedure(models.Model):
    # فیلدهای مربوط به روش‌های پرتودرمانی و انکولوژی
    name = models.CharField(max_length=100, verbose_name='نام روش پرتودرمانی و انکولوژی')
    description = models.TextField(verbose_name='توضیحات روش پرتودرمانی و انکولوژی')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class RadiationTest(models.Model):
    # فیلدهای مربوط به آزمایش‌های پرتودرمانی و انکولوژی
    name = models.CharField(max_length=100, verbose_name='نام آزمایش پرتودرمانی و انکولوژی')
    description = models.TextField(verbose_name='توضیحات آزمایش پرتودرمانی و انکولوژی')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class Treatment(models.Model):
    # بیمار مربوط به این روند درمانی
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')

    # فیلدهای مربوط به روند پرتودرمانی و انکولوژی
    visit_date = models.DateTimeField(verbose_name='تاریخ ویزیت')
    symptoms = models.TextField(verbose_name='علائم بیماری')
    radiation_procedures = models.ManyToManyField(RadiationProcedure, blank=True, verbose_name='روش‌های پرتودرمانی و انکولوژی')
    radiation_tests = models.ManyToManyField(RadiationTest, blank=True, verbose_name='آزمایش‌های پرتودرمانی و انکولوژی')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"روند پرتودرمانی و انکولوژی بیمار {self.patient.full_name} در تاریخ {self.visit_date}"