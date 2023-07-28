from django.db import models

name = "Subspecialty Pain Medicine"

# مدل بیمار
class Patient(models.Model):
    # فیلدهای مربوط به بیمار
    full_name = models.CharField(max_length=100, verbose_name='نام کامل بیمار')
    age = models.PositiveIntegerField(verbose_name='سن')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.full_name

# مدل زیرتخصص درد (Pain Medicine)
class PainMedicine(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')
    pain_location = models.CharField(max_length=100, verbose_name='محل درد')
    pain_intensity = models.PositiveIntegerField(verbose_name='شدت درد')
    pain_description = models.TextField(verbose_name='توضیحات درد')
    pain_management_plan = models.TextField(verbose_name='طرح مدیریت درد')
    pain_medications = models.TextField(verbose_name='داروهای درد')
    pain_management_techniques = models.TextField(verbose_name='تکنیک‌های مدیریت درد')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"زیرتخصص درد برای بیمار {self.patient.full_name}"

# مدل تجویز (Treatment)
class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')
    description = models.TextField(verbose_name='توضیحات تجویز')
    date = models.DateField(verbose_name='تاریخ تجویز')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"تجویز برای بیمار {self.patient.full_name}"