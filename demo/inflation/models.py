# -*- coding: utf-8 -*-

from django.db import models


class Measurement(models.Model):
    date = models.DateField(verbose_name="Date")
    index = models.CharField(max_length=120, verbose_name="Index")
    value = models.FloatField(verbose_name="Value")
    month = models.CharField(max_length=60, verbose_name="Month")
