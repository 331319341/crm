from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from admin import OrderAdmin
# Create your views here.

def test(request):
    html = "<html><body>In hour(s), it will be .</body></html>"
    return render_to_response("admin/customer/test.html")
    return HttpResponse(html)