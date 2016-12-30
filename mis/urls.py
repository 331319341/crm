from django.conf.urls import include, url,static
from django.contrib import admin
from mis import settings
import workflow
import invent.urls
import basedata.urls
import selfhelp.urls
import mis
import customer.urls

urlpatterns = [
    # Examples:
    url(r'^$', 'mis.views.home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start",'workflow.views.start'),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)",'workflow.views.approve'),
    url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)",'workflow.views.restart'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/invent/', include(invent.urls)),
    url(r'^admin/basedata/', include(basedata.urls)),
    url(r'^admin/selfhelp/', include(selfhelp.urls)),
    url(r'^admin/customer/', include(customer.urls)),
]
urlpatterns += static.static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
