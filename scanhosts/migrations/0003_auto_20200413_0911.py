# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0002_auto_20200413_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browseinfo',
            name='useragent',
            field=models.CharField(verbose_name='用户浏览agent信息', max_length=512, null=True, default=''),
        ),
    ]
