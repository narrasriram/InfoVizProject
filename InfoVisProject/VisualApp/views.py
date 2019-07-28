"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from VisualApp.models import CanadaDataTemp
import json
from django.core.serializers.json import DjangoJSONEncoder

stat_list = CanadaDataTemp.objects.filter(data_year__in =('2010','2011','2012','2013','2014','2016','2017','2018')).values('stat_name','latitude','longitude','province','total_precip','data_month','data_year','yearmon')
print(type(stat_list))

def home(request):
    """Renders the home page."""

    climate_jsonObjects = []
    for info in stat_list:
        climate_jsonObjects.append(info)
    climate_jsonObjects = json.dumps(climate_jsonObjects, cls=DjangoJSONEncoder)
    print(climate_jsonObjects)
  
    context = {
                'title':'Home Page',
                'year':datetime.now().year,
                "stationObject": stat_list,
                } 


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',context
       )


def climate(request):
    print("Entered")
    climate_jsonObjects = []
    for info in stat_list:
        climate_jsonObjects.append(info)
    climate_jsonObjects = json.dumps(climate_jsonObjects, cls=DjangoJSONEncoder)
    print("Ended")                                                                                                                                                                                                                                                              
    return JsonResponse(list(stat_list),safe =False)