from django.contrib import admin
from .models import Applicant, Purpose, Cycle, ProcessingCenter, TreatmentFacility

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Purpose)
admin.site.register(Cycle)
admin.site.register(ProcessingCenter)
admin.site.register(TreatmentFacility)
