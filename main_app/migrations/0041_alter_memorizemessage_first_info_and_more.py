# Generated by Django 4.1.1 on 2023-09-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "main_app",
            "0040_remove_student_allah_names_student_allah_names_new_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="memorizemessage",
            name="first_info",
            field=models.JSONField(default=dict, null=True, verbose_name="الحفظ"),
        ),
        migrations.AlterField(
            model_name="memorizemessage",
            name="second_info",
            field=models.JSONField(
                default=dict, null=True, verbose_name="الحفظ قبل التعديل"
            ),
        ),
    ]
