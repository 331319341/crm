# -*- coding:utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from .models import Project, Customer, xiaoshou, Order, Contract
from common import generic

# Register your models here.

class XiaoshouInline(admin.TabularInline):
    model = xiaoshou
    
class CustomerAdmin(generic.BOAdmin):
    #list_display = ['name','leader']
    inlines = [XiaoshouInline]
    #fieldsets = [
     #   (None,{'fields':[(('projrcct',),('name','birth',),('gender','addr',),('phone',),('Email',),('QQ',),('xiaoshourenyuan',),('beizhu',))]}),
    #    (u'xsmx',{'fields':[(('amount', 'unit',),('xiaoshou', 'start_time',),('end_time', 'beizhu',))]})
    #]
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super(CustomerAdmin,self).save_model(request,obj,form,change)
            
    #def get_queryset(self, request):
    #    qs = super(MyModelAdmin, self).get_queryset(request)
    #    #if request.user.is_superuser:
    #    #    return qs
    #    return qs
    #    return qs.filter(reported_by_id=12)
    
class ProjectAdmin(generic.BOAdmin):
    list_display = ['title',]

class ContractAdmin(generic.BOAdmin):
    list_display = ['number', 'project_name', 'seller', 'customer_name', 'customer_ID', 'buy_date']
    fields = (('number',), ("into_way",), ('project_name',), ('seller',), ('customer_name',), ('customer_ID',), \
              ('bank_name',), ('bank_account',), ('buy_date',), ('buy_sum',), ('buy_category',), ('buy_deadline',), ('year_rate',))
    
    
class OrderAdmin(generic.BOAdmin):
    list_display = ['project_name','sale_leader', 'team_leader', 'seller', 'customer_name', 'start_time', 'manager']
    fields = (('project_name',), ('sale_leader',), ('team_leader',), ('seller',), ('customer_name',),
              ('start_time',), ('buy_sum',), ('buy_deadline',), ('year_rate',),
              ('commission_sale_leader', 'commission_sale_leader_rate', 'commission_sale_leader_sum',),
              ('commission_team_leader', 'commission_team_leader_rate', 'commission_team_leader_sum',),
              ('commission_deadline',),
              ('manager',))
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Order, OrderAdmin)
