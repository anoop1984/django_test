from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_fun(request):
     #return HttpResponse("Hello-World")
     return render(request,'index.html',{'name':'Anoop Singh Negi','link':'https://www.youtube.com/watch?v=ta9kgf15i20&t=3816s'})

def app1_fun1(request):
     return HttpResponse("Hello-Wold-2")

def app1_expression(request):

    a=request.POST['text1']
    b=request.POST['text2']
    c=int(a) + int(b)
    return render(request,'output.html', {'output':c})


def checking(request):
    return HttpResponse("Checking")
