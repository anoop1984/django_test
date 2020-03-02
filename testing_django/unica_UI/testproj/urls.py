"""testproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('pages/', include('pages.urls') ),
    path('loadjsonindb', views.loadjsonindb),
    path('dbtable', views.dbtable),
    path('dbtable_latest', views.dbtable_latest),
    path('dbtable_date',views.dbtable_info),

    #path('ajax', views.ajax),
    path('ajax', views.dbdata),
    path('ajax-post', views.ajax),
    path('', admin.site.urls),


]
