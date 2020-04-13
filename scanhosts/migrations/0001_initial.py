# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroweseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('useragent', models.CharField(verbose_name='用户浏览agent信息', max_length=100, null=True, default='')),
            ],
            options={
                'verbose_name': '用户浏览信息表',
                'verbose_name_plural': '用户浏览信息表',
                'db_table': 'browseinfo',
            },
        ),
        migrations.CreateModel(
            name='UserIPInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.CharField(verbose_name='ip地址', max_length=40, null=True, default='')),
                ('time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
            ],
            options={
                'verbose_name': '用户访问地址信息表',
                'verbose_name_plural': '用户访问地址信息表',
                'db_table': 'useripinfo',
            },
        ),
        migrations.AddField(
            model_name='broweseinfo',
            name='userip',
            field=models.ForeignKey(to='scanhosts.UserIPInfo'),
        ),
    ]
