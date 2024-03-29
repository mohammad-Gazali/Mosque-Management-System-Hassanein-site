# Generated by Django 4.1.1 on 2023-01-11 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "main_app",
            "0025_pointsadding_master_name_pointsdeletings_master_name_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="PointsAddingCause",
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
                ("name", models.CharField(max_length=255, verbose_name="الاسم")),
            ],
            options={
                "verbose_name": "سبب إضافة",
                "verbose_name_plural": "أسباب إضافة",
            },
        ),
        migrations.CreateModel(
            name="PointsDeleting",
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
                ("value", models.IntegerField(verbose_name="القيمة")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الخصم"),
                ),
            ],
            options={
                "verbose_name": "خصم نقاط",
                "verbose_name_plural": "خصومات النقاط",
            },
        ),
        migrations.CreateModel(
            name="PointsDeletingCause",
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
                ("name", models.CharField(max_length=255, verbose_name="الاسم")),
            ],
            options={
                "verbose_name": "سبب خصم",
                "verbose_name_plural": "أسباب خصم",
            },
        ),
        migrations.DeleteModel(
            name="PointsDeletings",
        ),
        migrations.AddField(
            model_name="pointsdeleting",
            name="cause",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main_app.pointsdeletingcause",
                verbose_name="السبب",
            ),
        ),
        migrations.AddField(
            model_name="pointsdeleting",
            name="master_name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.master",
                verbose_name="اسم الأستاذ",
            ),
        ),
        migrations.AddField(
            model_name="pointsdeleting",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.student",
                verbose_name="الطالب",
            ),
        ),
        migrations.AddField(
            model_name="pointsadding",
            name="cause",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main_app.pointsaddingcause",
                verbose_name="السبب",
            ),
        ),
    ]
