# Generated by Django 4.2.6 on 2023-10-18 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0003_alter_level_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='content',
        ),
    ]