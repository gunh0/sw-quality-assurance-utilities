# Generated by Django 2.0.2 on 2018-03-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.IntegerField(blank=True, null=True, verbose_name='목표매출')),
                ('currnet', models.IntegerField(blank=True, null=True, verbose_name='현재매출')),
                ('motto', models.CharField(max_length=30, verbose_name='좌우명')),
            ],
        ),
    ]