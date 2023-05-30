from django.contrib import admin
from .models import Event
from .models import Patient
from .models import Doctor

# Register your models here.

admin.site.register(Event)
admin.site.register(Patient)
admin.site.register(Doctor)