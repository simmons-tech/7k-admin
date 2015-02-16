# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0003_auto_20150216_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='filepath',
            field=models.FilePathField(path=b'/Users/larsj/Dropbox/Lars/MIT/spring2015/simmons-tech/7k-pics/', recursive=True),
            preserve_default=True,
        ),
    ]
