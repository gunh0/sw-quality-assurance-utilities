# Generated by Django 2.0.4 on 2018-05-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logperform', '0007_auto_20180509_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performagent',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='에이전트이름'),
        ),
    ]
