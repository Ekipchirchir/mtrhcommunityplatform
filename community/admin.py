from django.contrib import admin

# Register your models here.
from .models import Doctors, Nurses,SupportStaff, AlliedHealthProfessionals
admin.site.register(Doctors)
admin.site.register(Nurses)
admin.site.register(SupportStaff)
admin.site.register(AlliedHealthProfessionals)