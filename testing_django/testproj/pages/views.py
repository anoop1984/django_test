from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reqeust):
    return render(reqeust, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def index2(request):
    return render(request, 'pages/index2.html')


def index3(request):
    return render(request, 'pages/index3.html')

def healtcheck(request):
    return render(request, 'admin/healthcheck.html')


#def loadjsonindb(request):
#    return HttpResponse("Testing..Done!")


import json
def loadjsonindb(request):
    if request.method == "POST":
       text = request.POST['text']

       test_json = json.loads(text)

       from . models import healthCheck
       #from datetime import datetime
       import datetime 
    #   datet = datetime.now()
       datet = datetime.date(2020, 2, 2) 
       for item in test_json:
          ip = item['IPAddress'].strip()
          healthCheck.objects.create(desc=item['Test Description'], severity=item['Severity'], ipaddr=ip, hostname=item['Hostname'], command=item['Command-Executed'], verdict=item['Verdict'], remarks=item['Remarks'],test_id=item['Test ID'],date=datet)
          
       #print(test_json) 
       #return HttpResponse(test_json[0]['Test_Description'])
       return HttpResponse("<em>DATA Stored</em>")
    else:
          
    #  return HttpResponse("<em>This is for Unica</em>")
      return render(request, 'upload.html')

