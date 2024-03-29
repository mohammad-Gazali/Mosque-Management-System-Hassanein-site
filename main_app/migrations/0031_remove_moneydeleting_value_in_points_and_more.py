# Generated by Django 4.1.1 on 2023-02-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0030_alter_moneydeleting_active_to_points"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="moneydeleting",
            name="value_in_points",
        ),
        migrations.AddField(
            model_name="moneydeleting",
            name="is_money_main_value",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="moneydeleting",
            name="value",
            field=models.IntegerField(null=True, verbose_name="القيمة"),
        ),
    ]
