from django.contrib import admin
from keepgreen.models import keepGreen

admin.site.site_header = "KeepGreen Admin"

class ContactAdmin(admin.ModelAdmin):
    
    model = keepGreen
    list_display = ('fname', 'lname', 'email', 'phone', 'message')
    search_fields = ["email"]

admin.site.register(keepGreen, ContactAdmin)