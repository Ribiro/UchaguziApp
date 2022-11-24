from django.contrib import admin
from .models import PollingStation, Candidate, POResult, CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","first_name","last_name","email","id_no", "assigned_polling_station")
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PollingStation)
admin.site.register(Candidate)
admin.site.register(POResult)