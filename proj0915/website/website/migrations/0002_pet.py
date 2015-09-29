# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet_name', models.CharField(max_length=20)),
                ('pet_type', models.CharField(max_length=15)),
                ('pet_color', models.CharField(max_length=25)),
            ],
        ),
    ]
