# Generated by Django 4.1.1 on 2023-08-18 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0034_remove_student_q_test_candidate_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coming",
            name="note",
        ),
    ]
