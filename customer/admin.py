# -*- coding:utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from .models import Project, Customer, Order, Contract
from team.models import Employee, Team
from common import generic
from django.conf.urls import include, url
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
# Register your models here.

class CustomerAdmin(generic.BOAdmin):
    #list_display = ['name','leader']
    #fieldsets = [
     #   (None,{'fields':[(('projrcct',),('name','birth',),('gender','addr',),('phone',),('Email',),('QQ',),('xiaoshourenyuan',),('beizhu',))]}),
    #    (u'xsmx',{'fields':[(('amount', 'unit',),('xiaoshou', 'start_time',),('end_time', 'beizhu',))]})
    #]
            
    def get_queryset(self, request):
        qs = super(CustomerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        employee = Employee.objects.get(name=request.user)
        teams = Team.objects.filter(team_leader = employee.id)
        if teams:
            teamid_list = [i.id for i in teams]
            employees = Employee.objects.filter(team__in=teamid_list)
            seller_list = [i.id for i in employees]
            return qs.filter(seller__in=seller_list)
        return qs.filter(seller=employee.id)
    
class ProjectAdmin(generic.BOAdmin):
    list_display = ['title',]

class ContractAdmin(generic.BOAdmin):
    list_display = ['number', 'project_name', 'seller', 'customer_name', 'customer_ID', 'buy_date']
    fields = (('number',), ("into_way",), ('project_name',), ('seller',), ('customer_name',), ('customer_ID',), \
              ('bank_name',), ('bank_account',), ('buy_date',), ('buy_sum',), ('buy_category',), ('buy_deadline',), ('year_rate',))
    
    
class OrderAdmin(generic.BOAdmin):
    actions = ["list_order"]
    
    def list_order(self, request, queryset):
        response = HttpResponse()
        return response
    
    list_order.short_description = _("list_order")
    
    '''
    def get_urls(self):
        urls = super(OrderAdmin, self).get_urls()
        my_url = [url(r"^test/$", self.admin_site.admin_view(self.test)),]
        return my_url+urls
    
    def test(self, request):
        #qs = super(OrderAdmin, self).changelist_view(request)
        qs = super(OrderAdmin, self).get_queryset(request)
        print qs
        return render_to_response("admin/customer/test.html")
    '''
    
    list_display = ['project_name','sale_leader', 'team_leader', 'seller', 'customer_name', 'start_time', 'manager']
    fields = (('project_name',), ('sale_leader',), ('team_leader',), ('seller',), ('customer_name',),
              ('start_time',), ('buy_sum',), ('buy_deadline',), ('year_rate',),
              ('commission_sale_leader', 'commission_sale_leader_rate', 'commission_sale_leader_sum',),
              ('commission_team_leader', 'commission_team_leader_rate', 'commission_team_leader_sum',),
              ('commission_deadline',),
              ('manager',))
    
    readonly_fields = ['commission_sale_leader_sum', 'commission_team_leader_sum']
    #extra_buttons = [{'href':'pay','title':_('pay')}]
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Order, OrderAdmin)
