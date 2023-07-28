from django.db import models

name = "Adult Endocrinology"

class Patient(models.Model):
    # فیلدهای مربوط به بیمار
    full_name = models.CharField(max_length=100, verbose_name='نام کامل بیمار')
    age = models.PositiveIntegerField(verbose_name='سن')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.full_name

class AdultEndocrinologyProcedure(models.Model):
    # فیلدهای مربوط به روش‌های غدد بالغین
    name = models.CharField(max_length=100, verbose_name='نام روش غدد بالغین')
    description = models.TextField(verbose_name='توضیحات روش غدد بالغین')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class AdultEndocrinologyTest(models.Model):
    # فیلدهای مربوط به آزمایش‌های غدد بالغین
    name = models.CharField(max_length=100, verbose_name='نام آزمایش غدد بالغین')
    description = models.TextField(verbose_name='توضیحات آزمایش غدد بالغین')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class Treatment(models.Model):
    # بیمار مربوط به این روند درمانی
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')

    # فیلدهای مربوط به روند غدد بالغین
    visit_date = models.DateTimeField(verbose_name='تاریخ ویزیت')
    symptoms = models.TextField(verbose_name='علائم بیماری')
    adult_endocrinology_procedures = models.ManyToManyField(AdultEndocrinologyProcedure, blank=True, verbose_name='روش‌های غدد بالغین')
    adult_endocrinology_tests = models.ManyToManyField(AdultEndocrinologyTest, blank=True, verbose_name='آزمایش‌های غدد بالغین')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"روند غدد بالغین بیمار {self.patient.full_name} در تاریخ {self.visit_date}"