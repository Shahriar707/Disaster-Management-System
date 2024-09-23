from django.contrib import admin
from .models import Donation, Crisis, Volunteer, Inventory

# Register your models here.

class CrisisAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'description', 'required_help', 'is_approved']
    list_filter = ['is_approved', 'severity', 'status']

admin.site.register(Donation)
admin.site.register(Crisis, CrisisAdmin)
admin.site.register(Volunteer)
admin.site.register(Inventory)

# The admin.py file has register four models created in the models.py and also customized the admin interface through CrisisAdmin class 