# Generated by Django 4.1.1 on 2022-09-30 15:57

from django.db import migrations, models
import django.db.models.deletion
from main_app.default_json import json_default_value, json_default_value_two, json_default_value_three


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="الفئة")),
            ],
            options={
                "verbose_name": "الفئة",
                "verbose_name_plural": "الفئات",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=511, verbose_name="الاسم الثلاثي"),
                ),
                (
                    "mother_name",
                    models.CharField(max_length=255, verbose_name="اسم الأم"),
                ),
                (
                    "birthdate",
                    models.DateField(
                        blank=True, null=True, verbose_name="تاريخ الميلاد"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=511,
                        null=True,
                        verbose_name="العنوان تفصيلاً",
                    ),
                ),
                (
                    "static_phone",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="الهاتف الأرضي",
                    ),
                ),
                (
                    "cell_phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="الجوال"
                    ),
                ),
                (
                    "father_phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="جوال الأب"
                    ),
                ),
                (
                    "mother_phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="جوال الأم"
                    ),
                ),
                (
                    "registered_at",
                    models.DateField(auto_now_add=True, verbose_name="تاريخ التسجيل"),
                ),
                (
                    "father_work",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="عمل الأب"
                    ),
                ),
                (
                    "notes",
                    models.CharField(
                        blank=True, max_length=511, null=True, verbose_name="ملاحظات"
                    ),
                ),
                (
                    "school_class",
                    models.IntegerField(
                        choices=[
                            (-1, "غير محدد"),
                            (0, "روضة"),
                            (1, "أول"),
                            (2, "ثاني"),
                            (3, "ثالث"),
                            (4, "رابع"),
                            (5, "خامس"),
                            (6, "سادس"),
                            (7, "سابع"),
                            (8, "ثامن"),
                            (9, "تاسع"),
                            (10, "عاشر"),
                            (11, "حادي عشر"),
                            (12, "بكالوريا"),
                            (13, "جامعي"),
                            (14, "غير ذلك"),
                        ],
                        default=-1,
                        verbose_name="الصف",
                    ),
                ),
                (
                    "bring_him",
                    models.CharField(
                        blank=True, max_length=511, null=True, verbose_name="أحضره"
                    ),
                ),
                (
                    "q_memorizing",
                    models.JSONField(
                        default=json_default_value,
                        verbose_name="حفظ القرآن",
                    ),
                ),
                (
                    "q_test",
                    models.JSONField(
                        default=json_default_value_two,
                        verbose_name="السبر في المسجد",
                    ),
                ),
                (
                    "q_test_candidate",
                    models.JSONField(
                        default=json_default_value_three,
                        verbose_name="السبر الترشيحي",
                    ),
                ),
                (
                    "is_q_test_certificate",
                    models.BooleanField(default=True, verbose_name="هل يوجد سبر"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main_app.category",
                        verbose_name="الفئة",
                    ),
                ),
            ],
            options={
                "verbose_name": "الطالب",
                "verbose_name_plural": "الطلاب",
            },
        ),
        migrations.CreateModel(
            name="MemorizeNotes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "master_name",
                    models.CharField(max_length=511, verbose_name="اسم الأستاذ"),
                ),
                ("content", models.TextField()),
                (
                    "sended_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="تاريخ الإرسال"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل"),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.student",
                        verbose_name="اسم الطالب",
                    ),
                ),
            ],
            options={
                "verbose_name": "ملاحظة تسميع",
                "verbose_name_plural": "ملاحظات التسميع",
            },
        ),
        migrations.CreateModel(
            name="MemorizeMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "master_name",
                    models.CharField(max_length=255, verbose_name="اسم الأستاذ"),
                ),
                (
                    "sended_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="تاريخ الإرسال"
                    ),
                ),
                ("q_memo", models.JSONField(default=dict, verbose_name="التسميع")),
                (
                    "q_memo_before_edit",
                    models.JSONField(default=dict, verbose_name="التسميع قبل التعديل"),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.student",
                        verbose_name="اسم الطالب",
                    ),
                ),
            ],
            options={
                "verbose_name": "رسالة تسميع",
                "verbose_name_plural": "رسائل التسميع",
            },
        ),
    ]
