# Generated by Django 4.1.1 on 2023-02-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_moneydeleting'),
        ('specializtions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specializtion',
            name='students',
            field=models.ManyToManyField(blank=True, to='main_app.student', verbose_name='الطلاب'),
        ),
    ]
