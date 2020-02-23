from django.shortcuts import render
from django.contrib.auth.models  import User
from django.http import HttpResponse
# Create your views here.

def ser(request):
  print("nothing")
  return HttpResponse("testng")

def service(request):
  return render(request,'service.html')
  if request.method == 'POST':
     name = request.POST('name')
     description = request.POST('desc')
     service = request.POST('serc')
     status = request.POST('status')
   
     x = User.objects.create_user(name=name,description=description,service=service,status=status)
     x.save()
     print("Service Created")

  else:
    return render(request,'service.html')

def submit(request):
    return HttpResponse("Service Data Submitted to DB")
