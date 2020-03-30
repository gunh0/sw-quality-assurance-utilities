# Generated by Django 2.0.3 on 2018-03-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionauto', '0004_auto_20180327_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='testreserve',
            name='state',
            field=models.CharField(choices=[('RE', '예약'), ('AC', '접수'), ('PR', '진행'), ('CP', '완료')], default='RE', max_length=2, verbose_name='상태'),
        ),
    ]
