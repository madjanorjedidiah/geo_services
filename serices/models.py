# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.contrib.gis.db import models


class Regions(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)  # This field type is a guess.
    region = models.CharField(max_length=50, blank=True, null=True)
    number_of_providers = models.IntegerField(default=0)
    number_of_districts = models.IntegerField(default=0)
    budget = models.FloatField(default=0.00, null=True)
    priority = models.CharField(max_length=15, default='No')
    # capital = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'regions'



class Districts(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    district_n = models.CharField(max_length=29, blank=True, null=True)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True)
    number_of_providers = models.IntegerField(default=0)
    budget = models.FloatField(default=0.00, null=True)
    priority = models.CharField(max_length=15, default='No')
    referred_cases = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'districts'


class DistrictCapitals(models.Model):
    geom = models.PointField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    adm2_en = models.CharField(max_length=50, blank=True, null=True)
    adm2_pcode = models.CharField(max_length=50, blank=True, null=True)
    adm2_ref = models.CharField(max_length=50, blank=True, null=True)
    adm2alt1en = models.CharField(max_length=50, blank=True, null=True)
    adm2alt2en = models.CharField(max_length=50, blank=True, null=True)
    adm1_en = models.CharField(max_length=50, blank=True, null=True)
    adm1_pcode = models.CharField(max_length=50, blank=True, null=True)
    adm0_en = models.CharField(max_length=50, blank=True, null=True)
    adm0_pcode = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    validon = models.DateField(blank=True, null=True)
    validto = models.DateField(blank=True, null=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_capitals'