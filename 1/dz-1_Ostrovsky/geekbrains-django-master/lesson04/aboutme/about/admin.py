from django.contrib import admin

# Register your models here.
from .models import Company, Work, Description, UserProfile, Education, AboutDescription


class WorkInline(admin.StackedInline):
    model = Work
    extra = 2


class DescriptionInline(admin.StackedInline):
    model = Description
    extra = 5


class CompanyAdmin(admin.ModelAdmin):
    inlines = [WorkInline]
    list_display = ('short_name', 'address', 'website')


class WorkAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Description)
admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(AboutDescription)
