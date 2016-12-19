from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from .models import Project, Customer, xiaoshou

# Register your models here.

class XiaoshouInline(admin.TabularInline):
    model = xiaoshou

class CustomerAdmin(admin.ModelAdmin):
    #list_display = ['name','leader']
    inlines = [XiaoshouInline]
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super(TeamAdmin,self).save_model(request,obj,form,change)
            
    #def get_queryset(self, request):
    #    qs = super(MyModelAdmin, self).get_queryset(request)
    #    #if request.user.is_superuser:
    #    #    return qs
    #    return qs
    #    return qs.filter(reported_by_id=12)
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project)