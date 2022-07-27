from django.contrib import admin
from contact.models import ContactUs
# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_solved')
    list_display_links = ('id', 'name')

admin.site.register(ContactUs, AdminContact)