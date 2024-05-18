# Generated by Django 4.2.6 on 2024-05-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0055_alter_assetfile_category_alter_assetfile_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('last_name', models.CharField(max_length=255, verbose_name='الكنية')),
                ('father_name', models.CharField(max_length=255, verbose_name='اسم الأب')),
                ('mother_name', models.CharField(max_length=255, verbose_name='اسم الأم')),
                ('birthdate', models.DateField(verbose_name='تاريخ الميلاد')),
                ('static_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='الهاتف الأرضي')),
                ('cell_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='الجوال')),
                ('father_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='جوال الأب')),
                ('mother_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='جوال الأم')),
                ('father_work', models.CharField(blank=True, max_length=255, null=True, verbose_name='عمل الأب')),
                ('notes', models.CharField(blank=True, max_length=511, null=True, verbose_name='ملاحظات')),
            ],
            options={
                'verbose_name': 'طالب جديد',
                'verbose_name_plural': 'طلاب جدد',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='registered',
            field=models.BooleanField(default=False, verbose_name='مسجل السنة'),
        ),
    ]
