# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='person',
            field=models.ForeignKey(default=1, to='website.Person'),
            preserve_default=False,
        ),
    ]
