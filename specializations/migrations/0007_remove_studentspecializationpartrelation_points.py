# Generated by Django 4.2.6 on 2023-10-18 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0006_studentspecializationpartrelation_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentspecializationpartrelation',
            name='points',
        ),
    ]
