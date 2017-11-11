
from __future__ import unicode_literals

from django.db import models


class Albums(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums'

class Genre(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Libruary(models.Model):
    track_no = models.IntegerField(blank=True, null=True)
    track_name = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=80, blank=True, null=True)
    album = models.CharField(max_length=80, blank=True, null=True)
    genre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'libruary'
