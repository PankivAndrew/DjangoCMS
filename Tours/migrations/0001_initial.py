# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('NameOfImage', models.CharField(max_length=100)),
                ('ImagesID', models.CharField(null=True, max_length=100)),
                ('TourImage', models.ImageField(null=True, upload_to='Tours/Images')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('NameOfTour', models.CharField(null=True, max_length=2000)),
                ('DateOfTour', models.DateField(null=True)),
                ('PriceOfTour', models.DecimalField(decimal_places=2, null=True, max_digits=6)),
                ('IsScheduled', models.NullBooleanField()),
                ('TimeOfStarting', models.TimeField(null=True)),
                ('Description', models.TextField(null=True)),
                ('TourID', models.CharField(serialize=False, primary_key=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfTour',
            fields=[
                ('NameOfTour', models.CharField(null=True, max_length=100)),
                ('TypeOfTourID', models.CharField(serialize=False, primary_key=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='TypeOfTour',
            field=models.ForeignKey(null=True, to='Tours.TypeOfTour'),
        ),
        migrations.AddField(
            model_name='images',
            name='Tour',
            field=models.ForeignKey(null=True, to='Tours.Tour'),
        ),
    ]
