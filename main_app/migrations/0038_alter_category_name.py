# Generated by Django 4.1.1 on 2023-08-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0037_alter_student_mother_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, unique=True, verbose_name="الفئة"),
        ),
    ]
