from django.shortcuts import render
from django.http import HttpResponse

def test(request):
#   render(request,'service.html')
    return HttpResponse("testng")


def test1(request):
    return render(request,'json.html')
   

from django.http import JsonResponse
import json

def send_json(request):

  #  data = [{'name': 'Peter', 'email': 'peter@example.org'},
   #         {'name': 'Julia', 'email': 'julia@example.org'}]

    #return JsonResponse(data, safe=False)

  with open('/home/negi_anoopsingh/Djagno/webserver/templates/log.json','r') as f:
  #  data= json.loads(f)
  #return JsonResponse(data, safe=False)
   return HttpResponse(f)
