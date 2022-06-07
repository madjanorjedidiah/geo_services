from . import views
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . views import *


urlpatterns = [
	path('', views.welcome, name='welcome'),
	path('regions', views.regions_layer.as_view(), name='regions'),
	path('districts', views.districts_layer.as_view(), name='districts'),
	path('dist_capitals', views.district_cap_layer.as_view(), name='dist_capitals'),
]