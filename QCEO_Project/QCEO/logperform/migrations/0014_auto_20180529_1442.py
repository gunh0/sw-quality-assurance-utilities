# Generated by Django 2.0.4 on 2018-05-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logperform', '0013_auto_20180529_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performagent',
            name='ostype',
            field=models.CharField(blank=True, max_length=20, verbose_name='OS'),
        ),
    ]
