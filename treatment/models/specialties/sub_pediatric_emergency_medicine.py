from django.db import models

name = "Subspecialty Pediatric Emergency Medicine"

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

# مدل زیرتخصص پزشکی اورژانس کودکان (Pediatric Emergency Medicine)
class PediatricEmergencyMedicine(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')
    emergency_condition = models.TextField(verbose_name='وضعیت اورژانسی')
    treatment_plan = models.TextField(verbose_name='طرح درمانی اورژانسی')
    # فیلدهای مربوط به زیرتخصص اورژانس کودکان
    # ...

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"زیرتخصص پزشکی اورژانس کودکان برای بیمار {self.patient.full_name}"

# مدل تجویز (Treatment)
class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')
    description = models.TextField(verbose_name='توضیحات تجویز')
    date = models.DateField(verbose_name='تاریخ تجویز')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"تجویز برای بیمار {self.patient.full_name}"