from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import json

# Create your views here.
def current_date_time(request):
	return HttpResponse(json.dumps({"date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.Z')}), content_type="application/json")
