from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .models import Patient
from .models import Doctor

def events_view(request):
    # Get all patients and appointments
    patients = Patient.objects.all()
    events = Event.objects.all()
    context = {
        'events'  : Event,
        'patients' : Patient,
        'doctors' : Doctor,
        'title' : 'home'
    }



def home(request):
    context = {
        'events'  : Event,
        'patients' : Patient,
        'doctors' : Doctor,
        'title' : 'home'
    }
    return render(request, "clinic/home.html", context)

def doctor(request):
    context = {
        'events'  : Event,
        'patients' : Patient,
        'doctors' : Doctor,
        'title' : 'doctor',
        'searched_events' : []
    }
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id')
        if patient_id:
            # Search for appointments by patient ID
            searched_events = Event.objects.filter(patient_id=patient_id)
            return render(request, "clinic/doctor.html", {
                'patients': Patient,
                'events': Event,
                'searched_events': searched_events,
                'patient_id': patient_id
            })

    return render(request, "clinic/doctor.html",context)


def patient(request):
    context = {
        'events'  : Event,
        'patients' : Patient,
        'doctors' : Doctor,
        'title' : 'patient'
    }
    return render(request, "clinic/patient.html",context)

# Create your views here.
