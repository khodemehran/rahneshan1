from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import formola
from django.utils.translation import ugettext_lazy
# Register your models here.
#@admin.register(Category)
#class Cat_gory(admin.ModelAdmin):

  #  list_display = ('Name', 'slug',)
   # list_filter = ('Name',)
    #search_fields = ('Name',)


#@admin.register(farmer)
#class FarmerAdmin(admin.ModelAdmin):

 #   list_display = ('Category', 'User', 'created_at',)
  #  list_filter = ('Category', 'created_at', 'User')
   # search_fields = ('Name', 'Category')
    #raw_id_fields = ('User',)
    #date_hierarchy = 'created_at'
    #ordering = ('created_at',)
admin.site.register(formola)