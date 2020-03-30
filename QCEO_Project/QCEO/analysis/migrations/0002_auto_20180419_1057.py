# Generated by Django 2.0.4 on 2018-04-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestdefact',
            name='case',
            field=models.FileField(blank=True, upload_to='', verbose_name='케이스 생성'),
        ),
        migrations.AlterField(
            model_name='bestdefact',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='bestdefact',
            name='item',
            field=models.CharField(max_length=10, verbose_name='대항목'),
        ),
        migrations.AlterField(
            model_name='bestdefact',
            name='miditem',
            field=models.CharField(max_length=10, verbose_name='중항목'),
        ),
        migrations.AlterField(
            model_name='bestdefact',
            name='reference',
            field=models.TextField(verbose_name='참고항목'),
        ),
        migrations.AlterField(
            model_name='bestdefact',
            name='subitem',
            field=models.CharField(max_length=10, verbose_name='소항목'),
        ),
    ]
