from django.contrib import admin
from .models import DoctorList, MasterDoctorList, SalesRep, VisitPlan, DoctorVisit, Region, Product, Supervisor
# Register your models here.

admin.site.register(DoctorList)
admin.site.register(SalesRep)
admin.site.register(MasterDoctorList)
admin.site.register(VisitPlan)
admin.site.register(DoctorVisit)
admin.site.register(Region)
admin.site.register(Product)
admin.site.register(Supervisor)