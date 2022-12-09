from django.contrib import admin
from .models import PollingStation, Candidate, POResult

# Register your models here.
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ("first_name","last_name", "username", "email","id_no", "assigned_polling_station")
    
# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PollingStation)
admin.site.register(Candidate)
# admin.site.register(POResult)