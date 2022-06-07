from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import datetime
from .models import *
from django.contrib.gis.db.models import *
from djgeojson.views import GeoJSONLayerView
from django.core.serializers import serialize
import json



def welcome(request):
	return HttpResponse(' Welcome to services apis ')


#   Using this GeoJson's
class regions_layer(GeoJSONLayerView):
	# Options
	model = Regions
	precision = 4  
	simplify = 0.0001
	properties = ('geom', 'region')

	def get_queryset(self):
	    qs = super(regions_layer, self).get_queryset()
	    return qs


#   Using this GeoJson's
class districts_layer(GeoJSONLayerView):
	# Options
	model = Districts
	precision = 4  
	simplify = 0.0001
	properties = ('geom', 'district_n')

	def get_queryset(self):
	    qs = super(districts_layer, self).get_queryset()
	    return qs


#   Using this GeoJson's
class district_cap_layer(GeoJSONLayerView):
	# Options
	model = DistrictCapitals
	precision = 4  
	simplify = 0.0001
	properties = ('geom', 'adm2_en')

	def get_queryset(self):
	    qs = super(district_cap_layer, self).get_queryset()
	    return qs