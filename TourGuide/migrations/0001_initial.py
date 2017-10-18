# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourGuide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='TourGuide/Images')),
                ('Description', models.TextField()),
            ],
        ),
    ]
