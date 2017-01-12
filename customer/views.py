#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from customer.models import Order
import xlwt
from django.utils.text import force_text
# Create your views here.

def list_order(request):
    qs = Order.objects.all()
    for item in qs:
        item.commission_sale_leader_sum = float('%.2f' % ((item.buy_sum * item.commission_sale_leader_rate * 1.0)/100))
        item.commission_team_leader_sum = float('%.2f' % ((item.buy_sum * item.commission_team_leader_rate * 1.0)/100))
        item.save()
    result = {'list_item': qs}
    return render_to_response("admin/customer/list_order.html", result)
    
def payment_contract(request):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet("核算结果")
    
    field_list = [u"销售项目", u"往来账户", u"入账途径", u"合同编号", u"销售网点",
                  u"销售人员", u"客户姓名", u"客户性质", u"身份证号", u"开户行", u"账号",
                  u"起息时间", u"购买金额", u"认购类别", u"认购期限", u"年化业绩",
                  u"年利率", u"剩余应付天数", u"应付日期", u"应付本息金额", u"实付日期",
                  u"实付金额", u"付款警示", u"应付余额", u"应付总额"]
    for i in xrange(len(field_list)):
        sheet.write(0, i, field_list[i])
    Contract_list = Contract.objects.all()
    for item in Contract_list:
        will_pay_date = ''
        will_pay_sum = 0
        row_list = [item.project_name, '', item.into_way, item.number, '',
                    item.seller, item.customer_name, '', item.customer_ID, item.bank_name, item.bank_account,
                    item.buy_date, item.buy_sum, item.buy_category, item.buy_deadline, '',
                    item.year_rate, '', will_pay_date, will_pay_sum, '',
                    '', '', '', ''
                   ]
        for j in xrange(len(row_list)):
            sheet.write(0, j, row_list[j])
    response = HttpResponse(content_type='application/vnd.ms-excel')
    file_name = u"兑付核算"
    nn = urlquote(file_name)
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % nn
    workbook.save(response)
    return response