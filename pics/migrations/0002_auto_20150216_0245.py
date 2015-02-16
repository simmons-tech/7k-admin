# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='filepath',
            field=models.FilePathField(verbose_name=b'/Users/larsj/Dropbox (Personal)/Lars/MIT/spring2015/simmons-tech/7k-pics/', recursive=True),
            preserve_default=True,
        ),
    ]
