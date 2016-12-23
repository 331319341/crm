# -*- coding:utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
<<<<<<< HEAD
from django.forms import ModelForm,ChoiceField
=======
>>>>>>> bd684caf87842bf8907f440389fc184adf5a657b
from common import generic
from common import const
from .models import Team, Employee
from common import generic
from common.logger import logger
from common.permission_resource import add_team_permission, change_team_permission, delete_team_permission,\
                                       add_order_permission, change_order_permission, delete_order_permission, \
                                       add_customer_permission, change_customer_permission, delete_customer_permission

# Register your models here.

class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 0
    fields= ('name',)
    readonly_fields = ['name',]
    
<<<<<<< HEAD
class TeamForm(ModelForm):
    """

    """
    team_leader = ChoiceField(label=_("leader name"),choices=const.get_employee)
    class Meta:
        model = Team
        fields = ['name', 'create_time', 'team_leader', 'description']

    
=======
>>>>>>> bd684caf87842bf8907f440389fc184adf5a657b
class TeamAdmin(generic.BOAdmin):
    list_display = ['name', 'create_time', 'team_leader']
    fields = (('name'), ('create_time',), ('team_leader',), ('description',))
    inlines = [EmployeeInline,]
<<<<<<< HEAD
    form = TeamForm
    
=======
>>>>>>> bd684caf87842bf8907f440389fc184adf5a657b
    #def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #    extra_context = extra_context or {}
    #    extra_context.update(dict(readonly=True))
    #    return super(TeamAdmin,self).changeform_view(request,object_id,form_url,extra_context)
    
    def save_model(self, request, obj, form, change):
        if change:
            old_team = Team.objects.get(id=obj.id)
            if 'name' in form.changed_data:
                old_group = Group.objects.get(name=old_team.name)
                old_group.name = obj.name
                old_group.save()
            if 'team_leader' in form.changed_data:
                e = Employee.objects.get(id=obj.team_leader)
                e.team = old_team
                e.save()
            super(TeamAdmin, self).save_model(request,obj,form,change)
        else:
            team = Group()
            team.name = obj.name
            team.save()
            super(TeamAdmin, self).save_model(request,obj,form,change)
            if obj.team_leader:
                e = Employee.objects.get(id=obj.team_leader)
                e.team = obj
                e.save()
    
class EmployeeAdmin(generic.BOAdmin):
    list_display = ['name', 'team', 'enter_date']
    fields = (('name',), ('passwd',), ('team',), ('enter_date',))
    
    def get_actions(self, request):
        pass
    
    def delete_model(self, request, obj):
        print 'delete'
        print obj.id
        super(EmployeeAdmin, self).delete_model(request,obj)
        User.objects.filter(username=obj.name).delete()
    
    def save_model(self, request, obj, form, change):
        if change:
            old_employyee = Employee.objects.get(id=obj.id)
            old_user = User.objects.get(username=old_employyee.name)
            if 'name' in form.changed_data:
                old_user.username = obj.name
            if 'passwd' in form.changed_data:
                old_user.set_password(obj.passwd)
            old_user.save()
        else:
            user = User.objects._create_user(username=obj.name,
                                             email=None,
                                             password=obj.passwd,
                                             is_staff=True,
                                             is_superuser=False
                                           )
            user.save
            user.user_permissions.add(add_team_permission)
            #user.user_permissions.add(add_team_permission, change_team_permission, delete_team_permission)
            #user.user_permissions.add(add_order_permission, change_order_permission, delete_order_permission)
            user.user_permissions.add(add_customer_permission, change_customer_permission, delete_customer_permission)
        super(EmployeeAdmin, self).save_model(request,obj,form,change)
    
admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)