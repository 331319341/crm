from django.conf.urls import include, url,static
import customer.views

urlpatterns = [
    url(r"^order/list_order/$", 'customer.views.list_order'),
]
