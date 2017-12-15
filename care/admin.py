from django.contrib import admin
from .models import Cause, Physician, Profile, Patient

admin.site.register(Cause)
admin.site.register(Physician)
admin.site.register(Profile)
admin.site.register(Patient)
