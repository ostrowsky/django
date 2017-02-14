from django.contrib import admin
from .models import Organization, Work

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'in_msk', 'flag']

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Work)