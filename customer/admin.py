# -*- coding:utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from .models import Project, Customer, Order, Contract
from team.models import Employee, Team
from common import generic
import xlwt
import copy
from django.conf.urls import include, url
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.http import urlquote
from collections import OrderedDict
from .util import getdate, getJIKUANDate, getJIEKUANSum, mathsum

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
    actions = ["pay_contract"]
    def pay_contract(self, request, queryset):
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet("核算结果")
    
        field_list = [
                        u"销售项目", u"往来账户", u"入账途径", u"合同编号", u"销售网点",
                        u"销售人员", u"客户姓名", u"客户性质", u"身份证号", u"开户行",
                        u"账号", u"起息时间", u"购买金额", u"认购类别", u"认购期限",
                        u"年化业绩", u"年利率", u"剩余应付天数", u"应付日期", u"应付本息金额",
                        u"实付日期", u"实付金额", u"付款警示", u"应付余额", u"应付总额"]
        field_dict = ['project_name', 'contact_account', 'into_way', 'number', 'sales_network',
                      'seller', 'customer_name', 'customer_xingzhi', 'customer_ID', 'bank_name',
                      'bank_account', 'buy_date', 'buy_sum', 'buy_category', 'buy_deadline',
                      'nianhu', 'year_rate', 'SYDays', 'YFDate', 'YFSum',
                      'SFDate', 'SFSum', 'notice', 'YFYE', 'YFTotal']
        
        split_cell = ['SYDays', 'YFDate', 'YFSum', 'SFDate', 'SFSum', 'YFYE']
        
        for i in xrange(len(field_list)):
            sheet.write(0, i, field_list[i])
        Contract_list = Contract.objects.all()
        row_index = 1
        for item in Contract_list:
            one_contract = OrderedDict.fromkeys(field_dict)
            one_contract['project_name'] = item.project_name.title
            one_contract['into_way'] = item.into_way
            one_contract['number'] = item.number
            one_contract['seller'] = item.seller.name
            one_contract['customer_name'] = item.customer_name
            one_contract['customer_ID'] = item.customer_ID
            one_contract['bank_name'] = item.bank_name
            one_contract['bank_account'] = item.bank_account
            one_contract['buy_date'] = item.buy_date.strftime('%Y-%m-%d')
            one_contract['buy_sum'] = item.buy_sum
            one_contract['buy_category'] = item.buy_category
            one_contract['buy_deadline'] = item.buy_deadline
            one_contract['year_rate'] = item.year_rate
            
            row_list = []
            project_cata = item.project_name.cata
            year_rate = item.year_rate / 100.0
            if project_cata == '1': #基金项目
                month_count = item.buy_deadline
                t = month_count / 3
                for i in xrange(t):
                    buy_date = item.buy_date.strftime('%Y-%m-%d')
                    YFDate = getdate(buy_date, (i+1)*3)
                    YFSum = mathsum(item.buy_sum * year_rate / 4)
                    if i == t-1:
                        YFSum = YFSum + item.buy_sum
                    the_contract = copy.deepcopy(one_contract)
                    the_contract['YFDate'] = YFDate
                    the_contract['YFSum'] = YFSum
                    row_list.append(the_contract)
            elif project_cata == '2': #借款项目
                deadline = item.buy_deadline
                if deadline <= 3:
                    the_contract = copy.deepcopy(one_contract)
                    buy_date = item.buy_date.strftime('%Y-%m-%d')
                    the_contract['YFDate'] = getdate(buy_date, deadline)
                    the_contract['YFSum'] = mathsum(item.buy_sum + (item.buy_sum * year_rate * item.buy_deadline / 12))
                    row_list.append(the_contract)
                elif deadline >= 6:
                    buy_date = item.buy_date.strftime('%Y-%m-%d')
                    YFDate = getJIKUANDate(buy_date, item.buy_deadline)
                    YFSum = getJIEKUANSum(YFDate, item.buy_sum, buy_date, year_rate, item.buy_deadline)
                    for i in range(len(YFDate)):
                        the_contract = copy.deepcopy(one_contract)
                        the_contract['YFDate'] = YFDate[i]
                        the_contract['YFSum'] = YFSum[i]
                        row_list.append(the_contract)
                else:
                    pass
            
            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            alignment.vert = xlwt.Alignment.VERT_CENTER
            style1= xlwt.XFStyle()
            style1.alignment = alignment
            
            col = 0
            for k,v in row_list[0].items():
                if k not in  split_cell:
                    sheet.write_merge(row_index, row_index+len(row_list)-1, col, col, v, style1)
                col += 1
                
            for j in xrange(len(row_list)):
                col = 0
                for k,v in row_list[j].items():
                    if k in split_cell:
                        sheet.write(row_index, col, v)
                    col += 1
                row_index += 1
            
        response = HttpResponse(content_type='application/vnd.ms-excel')
        file_name = u"兑付核算"
        nn = urlquote(file_name)
        response['Content-Disposition'] = 'attachment; filename=%s.xls' % nn
        workbook.save(response)
        return response

    pay_contract.short_description = _("pay_contract")
    
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
