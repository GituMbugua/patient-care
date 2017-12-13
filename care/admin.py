from django.contrib import admin
from .models import Department, Profile, Patient

admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(Department)
