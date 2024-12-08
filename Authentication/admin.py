from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(DoctorSpecialization)
admin.site.register(GroupPermission)
admin.site.register(Administrator)
admin.site.register(patient)
admin.site.register(Organization)
