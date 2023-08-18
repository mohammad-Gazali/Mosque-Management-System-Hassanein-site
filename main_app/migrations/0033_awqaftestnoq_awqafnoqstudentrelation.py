# Generated by Django 4.1.1 on 2023-02-18 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0032_student_q_awqaf_test_explaining_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AwqafTestNoQ",
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
                ("name", models.CharField(max_length=511, verbose_name="الاسم")),
                ("points", models.IntegerField(verbose_name="النقاط")),
            ],
            options={
                "verbose_name": "سبر أوقاف بغير القرآن",
                "verbose_name_plural": "سبر الأوقاف بغير القرآن",
            },
        ),
        migrations.CreateModel(
            name="AwqafNoQStudentRelation",
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
                    "is_old",
                    models.BooleanField(default=False, verbose_name="هل السبر قديم"),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.student",
                        verbose_name="الطالب",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.awqaftestnoq",
                        verbose_name="سبر الأوقاف",
                    ),
                ),
            ],
        ),
    ]