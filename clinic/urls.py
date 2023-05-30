from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="clinic-home"),
    path('doctor/', views.doctor,name="clinic-doctor"),
    path('patient/', views.patient,name="clinic-patient"),
]