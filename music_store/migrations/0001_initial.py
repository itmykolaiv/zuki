# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=45, blank=True, null=True)),
            ],
            options={
                'db_table': 'albums',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80, blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'artists',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=45, blank=True, null=True)),
            ],
            options={
                'db_table': 'genre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Libruary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('track_no', models.IntegerField(blank=True, null=True)),
                ('track_name', models.CharField(max_length=255, blank=True, null=True)),
                ('artist', models.CharField(max_length=80, blank=True, null=True)),
                ('embed', models.TextField(blank=True, null=True)),
                ('album', models.CharField(max_length=80, blank=True, null=True)),
                ('genre', models.CharField(max_length=80, blank=True, null=True)),
            ],
            options={
                'db_table': 'libruary',
                'managed': True,
            },
        ),
    ]
