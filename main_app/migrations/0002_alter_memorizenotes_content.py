# Generated by Django 4.1.1 on 2022-10-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memorizenotes",
            name="content",
            field=models.CharField(max_length=511, verbose_name="المحتوى"),
        ),
    ]
