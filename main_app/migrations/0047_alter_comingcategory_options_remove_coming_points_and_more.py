# Generated by Django 4.1.1 on 2023-09-23 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0046_alter_studentgroup_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comingcategory",
            options={
                "verbose_name": "سبب الحضور",
                "verbose_name_plural": "أسباب الحضور",
            },
        ),
        migrations.RemoveField(
            model_name="coming",
            name="points",
        ),
        migrations.AddField(
            model_name="coming",
            name="is_doubled",
            field=models.BooleanField(default=False, verbose_name="القيمة مضاعفة"),
        ),
        migrations.AddField(
            model_name="comingcategory",
            name="points",
            field=models.IntegerField(default=10, verbose_name="قيمة النقاط"),
        ),
        migrations.AlterField(
            model_name="coming",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main_app.comingcategory",
                verbose_name="سبب الحضور",
            ),
        ),
    ]
