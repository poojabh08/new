"""hos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from home.views import home_view,printt,patientlogin,InPatient,createbill
from home.views import patientpage,receptionistlogin,ReceptionistPage,AReport,ABill,AToken,TokenT,createpatient,search
from home.views import TokenT,createpatient,register,doctorlogin

urlpatterns = [
    path('',home_view),
    path('admin/', admin.site.urls),
    path('Create/',createpatient),
    path('tokenT/<str:name>',TokenT),
    path('print/',printt),
    path('login-patient/',patientlogin,name="log"),
    path('patient/<str:name>',InPatient),
    path('createbill/',createbill),
    path('PatientPage/<str:name>',patientpage),
    path('login-r/',receptionistlogin),
    path('receptionist/<str:name>',ReceptionistPage),
    path('allReport/',AReport),
    path('allBill/',ABill),
    path('allToken/',AToken),
    path('Search/',search),
    path('R/',register),
    #path('r/',receptionistaccount),
    path('doctorlogin/',doctorlogin),
]
