# Generated by Django 4.1.1 on 2023-02-17 18:42

from django.db import migrations, models
from main_app.default_json import json_default_value_three


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0031_remove_moneydeleting_value_in_points_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="q_awqaf_test_explaining",
            field=models.JSONField(
                default=json_default_value_three,
                verbose_name="سبر القرآن تفسيراً في الأوقاف",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="q_awqaf_test_looking",
            field=models.JSONField(
                default=json_default_value_three,
                verbose_name="سبر القرآن نظراً في الأوقاف",
            ),
        ),
    ]
