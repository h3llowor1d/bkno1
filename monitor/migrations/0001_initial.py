# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chengfa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chengshu', models.IntegerField(verbose_name='\u4e58\u6570')),
                ('beichengshu', models.IntegerField(verbose_name='\u88ab\u4e58\u6570')),
                ('cfresult', models.IntegerField(verbose_name='\u7ed3\u679c')),
            ],
        ),
    ]
