# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filepath', models.FilePathField(verbose_name=b'/Users/larsj/Dropbox (Personal)/Lars/MIT/spring2015/simmons-tech/7k-pic', recursive=True, match=b'(*.jpg)|(*.png)')),
                ('title', models.CharField(max_length=300)),
                ('creator', models.CharField(max_length=32)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
