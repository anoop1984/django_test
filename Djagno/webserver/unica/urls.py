from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unica1/',views.unica1, name="unica1" ),
    path('unica1/loadjsonindb',views.loadjsonindb, name="unica1" ),
    path('loadfromdb/',views.loadfromdb, name="unica1" ),
]
