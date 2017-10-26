from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import json

# Create your views here.
def current_date_time(request):
	return HttpResponse(json.dumps({"date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.Z')}), content_type="application/json")

def current_date_time_page(request):
	return render(request, 'index.html', {'datetime': datetime.now().strftime('%Y/%m/%d %H:%M:%S')})