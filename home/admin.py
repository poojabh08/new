from django.contrib import admin
from home.models import patient,token,report,doctor,bill,receptionist
# Register your models here.

admin.site.register(patient)
admin.site.register(report)
admin.site.register(token)
admin.site.register(doctor)
admin.site.register(bill)
admin.site.register(receptionist)

