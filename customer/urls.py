from django.conf.urls import include, url,static
import customer.views

urlpatterns = [
    url(r"(?P<model>\w+)/add/$", 'customer.views.pay_action'),
]
