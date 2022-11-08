from django.contrib import admin
from .models import PollingStation, Candidate, Result

# Register your models here.
admin.site.register(PollingStation)
admin.site.register(Candidate)
admin.site.register(Result)