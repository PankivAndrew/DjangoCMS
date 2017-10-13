# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('WhoSent', models.CharField(max_length=100)),
                ('NameOfTour', models.CharField(max_length=200)),
                ('AmountOfPeople', models.IntegerField()),
                ('LanguageOfTour', models.CharField(max_length=100)),
                ('DateOfTour', models.DateField()),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
