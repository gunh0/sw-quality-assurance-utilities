# Generated by Django 2.0.4 on 2018-05-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logmonitor', '0012_auto_20180530_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringproduct',
            name='logpath',
            field=models.CharField(default='/', max_length=100, unique=True, verbose_name='운영체제'),
            preserve_default=False,
        ),
    ]
