from django.shortcuts import render
from django.http import HttpResponse

from . models import healthCheck

import json
from django.http import JsonResponse
import datetime

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



def loadjsonindb(request):
    if request.method == "POST":
       text = request.POST['text']

       test_json = json.loads(text)

    #   datet = datetime.now()
       datet = datetime.date(2020, 1, 20) 
       for item in test_json:
          ip = item['IPAddress'].strip()
          healthCheck.objects.create(desc=item['Test Description'], severity=item['Severity'], ipaddr=ip, hostname=item['Hostname'], command=item['Command-Executed'], verdict=item['Verdict'], remarks=item['Remarks'],test_id=item['Test ID'],date=datet)
          
       #print(test_json) 
       #return HttpResponse(test_json[0]['Test_Description'])
       return HttpResponse("<em>DATA Stored</em>")
    else:
      date_list = healthCheck.objects.values("date").distinct()
      print(date_list)
          
    #  return HttpResponse("<em>This is for Unica</em>")
      return render(request, 'upload.html',{'dates':date_list})



def dbtable(request):
    data = healthCheck.objects.all()
    data_dict = {'monitor_records': data }
    return render(request,'dbtable.html', context=data_dict)



def ajax1(request):
   test1 = "ajax-testing-successful"
   test2 = "wow"
   response = {}
   response['1']=test1
   response['2']=test2
   return JsonResponse(response)


def convert_date(date):
    date_lt = date.split(',')  
    print(date_lt)
    yy = date_lt[1].strip()
    print(yy)
    mm_dd = date_lt[0].split('.')
    print(mm_dd)
    dd = mm_dd[1].strip()
    print(dd)
    mm = mm_dd[0]
   
    mm = mm.lower()
    print(mm)
    if "jan" in mm: return yy+"-1-"+dd
    if "feb" in mm: return yy+"-2-"+dd
    if "mar" in mm: return yy+"-3-"+dd
    if "apr" in mm: return yy+"-4-"+dd
    if "may" in mm: return yy+"-5-"+dd
    if "jun" in mm: return yy+"-6-"+dd
    if "jul" in mm: return yy+"-7-"+dd
    if "aug" in mm: return yy+"-8-"+dd
    if "sep" in mm: return yy+"-9-"+dd
    if "oct" in mm: return yy+"-10-"+dd
    if "nov" in mm: return yy+"-11-"+dd
    if "dec" in mm: return yy+"-12-"+dd
   



   
    

def ajax(request):
    date = request.POST['date']
    #convert date string into YYYY-MM-DD formate
    
    date1=convert_date(date)    
    print(date1)
  
    print("hahaha: ",type(date1))
    testcount = healthCheck.objects.filter(date=date1).count()
    print("selected-date:", date)

    response={'date':date, 'test-count': testcount} 
    return JsonResponse(response)

    
    

def dbdata(request):
    data = healthCheck.objects.all().values()
    data1 = healthCheck.objects.filter(verdict__contains="Passed").values('remarks')
    severity_failed_major = healthCheck.objects.filter(severity__contains="Major",verdict__contains="Failed")
    severity_failed_minor = healthCheck.objects.filter(severity__contains="Minor",verdict__contains="Failed")
    severity_failed_catestrophic = healthCheck.objects.filter(severity__contains="Catestrophic",verdict__contains="Failed")
    severity_failed_warning = healthCheck.objects.filter(severity__contains="Warning",verdict__contains="Failed")

    #print(list(data))
    count_passed = len(data1)
    print("Passed Test Case",count_passed)
    fail = healthCheck.objects.filter(verdict__contains="Failed")
    print("Failed Test Case",len(fail))
    print("Total Test Case",len(data))
    date =(data[0])['date'].strftime('%m %B,%Y')
    result={}

    result['passed']=count_passed
    result['failed']=len(fail)
    result['total']=len(data)
    result['date']=date
    result['severity_failed_major']=len(severity_failed_major)
    result['severity_failed_minor']=len(severity_failed_minor)
    result['severity_failed_catestrophic']=len(severity_failed_catestrophic)
    result['severity_failed_warning']=len(severity_failed_warning)
   
    

    return JsonResponse(result)

    #data_dict = {'monitor_records': list(data) }
    #return JsonResponse(data_dict)


def strip_spaces(list_of_dict):
    final=[]
    for m in list_of_dict:
        temp = {}
        for k,v in m.items():
            temp[k]=str(v).strip()
        final.append(temp)
    return final



def refine_result(list_of_dict):
  final_dict = {}
  for item in list_of_dict:
    for k,v in item.items():
       if k in final_dict:
          final_dict[k].append(v)
       else:
          final_dict[k] = [v]	


  return final_dict





def dbdata1(request):
    
    return JsonResponse(result)

