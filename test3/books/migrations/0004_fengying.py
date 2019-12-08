# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_feng'),
    ]

    operations = [
        migrations.CreateModel(
            name='fengying',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fname', models.CharField(max_length=20)),
                ('dbdate', models.DateField()),
                ('hcomment', models.CharField(max_length=128)),
            ],
        ),
    ]
