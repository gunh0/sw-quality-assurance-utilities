# Generated by Django 2.0.4 on 2018-05-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logmonitor', '0006_auto_20180517_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringproduct',
            name='product',
            field=models.CharField(blank=True, choices=[('SecuMS', 'SecuMS'), ('OmniGuardUnix', 'OmniGuardUnix'), ('OmniGuardWindows', 'OmniGuardWindows'), ('FOSSGuard', 'FOSSGuard'), ('Athene', 'Athene')], max_length=30, verbose_name='제품'),
        ),
    ]