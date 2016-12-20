# -*- coding:utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const
from .models import Team, Employee
from common import generic
from common.logger import logger

# Register your models here.
    
class TeamAdmin(generic.BOAdmin):
    list_display = ['name', 'create_time', 'team_leader']
    fields = (('name'), ('create_time',), ('team_leader',), ('description',))
    
    def save_model(self, request, obj, form, change):
        logger.debug('save team')
        logger.debug('obj id:%s'% obj.id)
        logger.debug('obj name:%s'% obj.name)
        logger.debug('obj create_time:%s'% obj.create_time)
        logger.debug('obj team_leader:%s'% obj.team_leader)
        logger.debug('obj description:%s'% obj.description)
        logger.debug('form:%s' % dir(form))
        logger.debug('change:%s' % change)
        #if obj.parent and obj.parent.organization:
        #    obj.organization = obj.parent.organization
        #    obj.save()
        #super(TeamAdmin, self).save_model(request,obj,form,change)
    
class EmployeeAdmin(generic.BOAdmin):
    list_display = ['name', 'team', 'create_time']
    fields = (('name',), ('passwd',), ('team',), ('create_time',))

admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)