from django.db import models

name = "Pediatric Nephrology"

class Patient(models.Model):
    # فیلدهای مربوط به بیمار
    full_name = models.CharField(max_length=100, verbose_name='نام کامل بیمار')
    age = models.PositiveIntegerField(verbose_name='سن')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.full_name

class PediatricNephrologyProcedure(models.Model):
    # فیلدهای مربوط به روش‌های نفرولوژی کودکان
    name = models.CharField(max_length=100, verbose_name='نام روش نفرولوژی کودکان')
    description = models.TextField(verbose_name='توضیحات روش نفرولوژی کودکان')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class PediatricNephrologyTest(models.Model):
    # فیلدهای مربوط به آزمایش‌های نفرولوژی کودکان
    name = models.CharField(max_length=100, verbose_name='نام آزمایش نفرولوژی کودکان')
    description = models.TextField(verbose_name='توضیحات آزمایش نفرولوژی کودکان')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class Treatment(models.Model):
    # بیمار مربوط به این روند درمانی
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')

    # فیلدهای مربوط به روند نفرولوژی کودکان
    visit_date = models.DateTimeField(verbose_name='تاریخ ویزیت')
    symptoms = models.TextField(verbose_name='علائم بیماری')
    pediatric_nephrology_procedures = models.ManyToManyField(PediatricNephrologyProcedure, blank=True, verbose_name='روش‌های نفرولوژی کودکان')
    pediatric_nephrology_tests = models.ManyToManyField(PediatricNephrologyTest, blank=True, verbose_name='آزمایش‌های نفرولوژی کودکان')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"روند نفرولوژی کودکان بیمار {self.patient.full_name} در تاریخ {self.visit_date}"