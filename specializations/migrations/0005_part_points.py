# Generated by Django 4.2.6 on 2023-10-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0004_remove_level_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='points',
            field=models.IntegerField(default=30, verbose_name='النقاط'),
            preserve_default=False,
        ),
    ]
