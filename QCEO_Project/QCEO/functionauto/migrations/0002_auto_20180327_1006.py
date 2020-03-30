# Generated by Django 2.0.3 on 2018-03-27 01:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('functionauto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testreserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='예약자명')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='예약시간')),
                ('project', models.CharField(max_length=30, verbose_name='프로젝트명')),
                ('memo', models.TextField(blank=True, verbose_name='메모')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='등록')),
            ],
        ),
        migrations.AddField(
            model_name='autotest',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name='보고서'),
        ),
    ]
