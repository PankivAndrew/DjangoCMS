# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('DateOfNews', models.DateField(null=True)),
                ('NameOfNews', models.CharField(max_length=2000)),
                ('NewsID', models.CharField(primary_key=True, serialize=False, max_length=100)),
                ('HasVideo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Video', models.FileField(upload_to='News/Videos')),
                ('NameOfVideo', models.CharField(max_length=300)),
                ('VideoID', models.CharField(max_length=100)),
                ('News', models.ForeignKey(to='News.News', null=True)),
            ],
        ),
    ]
