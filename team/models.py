from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from common import generic
from common import const

# Create your models here.

class Team(generic.BO):
    name = models.CharField(verbose_name=_("team name"), max_length=32, unique=True)
    create_time = models.DateField(verbose_name=_("create time"))
    #team_leader = models.IntegerField(verbose_name=_("leader name"), null=True, blank=True, choices=const.get_employee())
    team_leader = models.IntegerField(verbose_name=_("leader name"), null=True, blank=True)
    description = models.CharField(verbose_name=_("team desc"), max_length=256, null=True)
    
    class Meta:
        verbose_name = _("sale team")
        verbose_name_plural = _("sale teams")
        
class Employee(generic.BO):
    name = models.CharField(verbose_name=_("name"), max_length=32, unique=True)
    passwd = models.CharField(verbose_name=_("passwd"), max_length=32)
    team = models.ForeignKey(Team, verbose_name=_("project team"), null=True, blank=True)
    enter_date = models.DateField(verbose_name=_("enter date"))
    
    class Meta:
        verbose_name = _("sale employee")
        verbose_name_plural = _("sale employees")