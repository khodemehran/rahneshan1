from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import PlanetData, Contact
from django.utils.translation import ugettext_lazy
# Register your models here.
@admin.register(PlanetData)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Category', 'User', 'created_at',)
    list_filter = ('Category', 'created_at', 'User')
    search_fields = ('Name', 'Category')
    raw_id_fields = ('User',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    site_title = ugettext_lazy('مدیریت سایت')

admin.site.site_header = 'مدیریت سایت'
@admin.register(Contact)
class ContantAdmin(admin.ModelAdmin):
    list_display = ('name','Email_field','content')
    list_filter = ('name','content')
