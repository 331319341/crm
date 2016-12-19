from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from .models import Task

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        #if request.user.is_superuser:
        #    return qs
        return qs
        return qs.filter(reported_by_id=12)

admin.site.register(Task, MyModelAdmin)