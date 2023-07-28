from django.db import models

name = "Craniofacial Surgery"

class Patient(models.Model):
    # فیلدهای مربوط به بیمار
    full_name = models.CharField(max_length=100, verbose_name='نام کامل بیمار')
    age = models.PositiveIntegerField(verbose_name='سن')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.full_name

class CraniofacialSurgeryProcedure(models.Model):
    # فیلدهای مربوط به روش‌های جراحی پلاستیک صورت
    name = models.CharField(max_length=100, verbose_name='نام روش جراحی پلاستیک صورت')
    description = models.TextField(verbose_name='توضیحات روش جراحی پلاستیک صورت')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return self.name

class Treatment(models.Model):
    # بیمار مربوط به این روند درمانی
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='بیمار')

    # فیلدهای مربوط به روند جراحی پلاستیک صورت
    craniofacial_surgery_procedures = models.ManyToManyField(CraniofacialSurgeryProcedure, blank=True, verbose_name='روش‌های جراحی پلاستیک صورت')

    # سایر فیلدهای مورد نیاز می‌توانند افزوده شوند

    def __str__(self):
        return f"روند جراحی پلاستیک صورت بیمار {self.patient.full_name}"