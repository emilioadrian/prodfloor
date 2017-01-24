# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodfloor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'My Jobs'},
        ),
        migrations.AddField(
            model_name='info',
            name='po',
            field=models.CharField(default=3320001, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stops',
            name='reason_description',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='features',
            name='features',
            field=models.CharField(choices=[('COP', 'Car Operating Panel'), ('SHC', 'Serial Hall Calls'), ('HAPS', 'HAPS battery'), ('OVL', 'Overlay'), ('GROUP', 'Group'), ('mView', 'mView'), ('iMon', 'iMonitor')], max_length=200),
        ),
        migrations.AlterField(
            model_name='info',
            name='current_index',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='stage_len',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stops',
            name='reason',
            field=models.CharField(choices=[('Reason 1', 'Reason 1'), ('Reason 2', 'Reason 2'), ('Reason 3', 'Reason 3'), ('Reason 4', 'Reason 4'), ('Reason 5', 'Reason 5'), ('Reason 6', 'Reason 6')], max_length=200),
        ),
    ]
