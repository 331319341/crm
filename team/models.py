from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Team(models.Model):
    name = models.CharField(verbose_name=_("team name"), max_length=32)
    create_time = models.DateField(verbose_name=_("create time"))
    team_leader = models.CharField(verbose_name=_("team name"), max_length=32)
    description = models.CharField(verbose_name=_("team desc"), max_length=256, null=True)
    
    class Meta:
        verbose_name = _("sale team")
        verbose_name_plural = _("sale teams")
        
class Employee(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=32)
    passwd = models.CharField(verbose_name=_("passwd"), max_length=32)
    team = models.ForeignKey(Team, verbose_name=_("project name"))
    create_time = models.DateField(verbose_name=_("create time"))
    
    class Meta:
        verbose_name = _("sale employee")
        verbose_name_plural = _("sale employees")