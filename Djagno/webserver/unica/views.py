from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def unica1(request):
    #return HttpResponse("<em>This is for Unica</em>")
    return render(request, 'upload.html')
    

import json
def loadjsonindb(request):
    if request.method == "POST":
       text = request.POST['text']

       test_json = json.loads(text)

       from . models import MonitorLog
       from datetime import datetime
       datet = datetime.now()
       for item in test_json:
          MonitorLog.objects.create(testDescription=item['Test Description'], severity=item['Severity'], ipaddress=item['IPAddress'], hostname=item['Hostname'], commandExecuter=item['Command-Executed'], verdict=item['Verdict'], remark=item['Remarks'],testId=item['Test ID'],timestamp=datet)
          
       #print(test_json) 
       #return HttpResponse(test_json[0]['Test_Description'])
       return HttpResponse("<em>DATA Stored</em>")
          
    return HttpResponse("<em>This is for Unica</em>")
   # return render(request, 'upload.html')



def loadfromdb(request):
    from . models import MonitorLog

    data = MonitorLog.objects.all()
    data_dict = {'monitor_records': data }
    return render(request,'dbtable.html', context=data_dict)
    
