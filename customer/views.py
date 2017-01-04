from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from customer.models import Order
# Create your views here.

def test(request):
    qs = Order.objects.all()
    for item in qs:
        item.commission_sale_leader_sum = float('%.2f' % ((item.buy_sum * item.commission_sale_leader_rate * 1.0)/100))
        item.commission_team_leader_sum = float('%.2f' % ((item.buy_sum * item.commission_team_leader_rate * 1.0)/100))
        item.save()
    result = {'list_item': qs}
    return render_to_response("admin/customer/test.html", result)