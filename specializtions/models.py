from django.db import models
from main_app.models import Student


class Specializtion(models.Model):
    name = models.CharField(max_length=511, verbose_name='الاسم')

    def __str__(self) -> str:
        return self.name

    
    class Meta:
        verbose_name = 'اختصاص'
        verbose_name_plural = 'الاختصاصات'


class Level(models.Model):
    level_number = models.IntegerField(default=1, verbose_name='رقم المستوى')
    specializtion = models.ForeignKey(Specializtion, verbose_name='الاختصاص', on_delete=models.CASCADE)
    content = models.CharField(max_length=1023, verbose_name='المحتوى')


    def __str__(self) -> str:
        return f"{self.specializtion}_المستوى_{self.level_number}"


    class Meta:
        verbose_name = 'مستوى'
        verbose_name_plural = 'المستويات'


class Part(models.Model):
    level = models.ForeignKey(Level, verbose_name='المستوى', on_delete=models.CASCADE)
    part_start = models.IntegerField(verbose_name='بداية القسم')
    part_end = models.IntegerField(verbose_name='نهاية القسم')
    part_number = models.IntegerField(default=1, verbose_name='ترتيب القسم')
    students = models.ManyToManyField(Student, verbose_name='الطلاب الذين أنهوا القسم', blank=True)

    def __str__(self) -> str:
        return f"{self.level.specializtion}_المستوى_{self.level.level_number}_القسم_{self.part_number}"

    
    class Meta:
        verbose_name = 'قسم'
        verbose_name_plural = 'أقسام'
