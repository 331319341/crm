#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from team.models import Employee
import datetime
from django.utils.translation import ugettext_lazy as _
from common import const
from common import generic

# Create your models here.
class Project(generic.BO):
    project_cata = (('1', u'基金项目'),('2', u'借款项目'))
    title = models.CharField(verbose_name=_("project name"), max_length=32)
    cata = models.CharField(verbose_name=_("project cata"), max_length=32, choices=project_cata, default='1')
    start_time = models.DateField(verbose_name=_("start time"), default=datetime.datetime.now)
    description = models.CharField(verbose_name=_("project desc"), max_length=256, null=True)
    
    class Meta:
        verbose_name = _("sale project")
        verbose_name_plural = _("sale projects")

class Customer(generic.BO):
    project = models.ForeignKey(Project, verbose_name=_("project name"))
    name = models.CharField(verbose_name=_("customer name"), max_length=32)
    birth = models.DateField(verbose_name=_("customer birth"))
    gender = models.CharField(verbose_name=_("customer gender"), max_length=8, choices=const.gender_set, default='1')
    addr = models.CharField(verbose_name=_("customer addr"), max_length=32)
    phone = models.CharField(verbose_name=_("phone"), max_length=16)
    Email = models.CharField(verbose_name=_("Email"), max_length=32)
    QQ = models.CharField(verbose_name=_("QQ"), max_length=16)
    seller = models.ForeignKey(Employee, verbose_name=_("seller"))
    beizhu = models.CharField(verbose_name=_("beizhu"), max_length=256)
    
    class Meta:
        verbose_name = _("sale customer")
        verbose_name_plural = _("sale customers")

class Order(models.Model):
    project_name = models.ForeignKey(Project, verbose_name=_("project name"))
    sale_leader = models.CharField(verbose_name=_("sale leader"), max_length=32)
    team_leader = models.CharField(verbose_name=_("team leader"), max_length=32)
    seller = models.ForeignKey(Employee, verbose_name=_("seller"))
    customer_name = models.CharField(verbose_name=_("customer name"), max_length=32)
    start_time = models.DateField(verbose_name=_("start time"), default=datetime.datetime.now)
    buy_sum = models.IntegerField(verbose_name=_("buy sum"))
    buy_deadline = models.IntegerField(verbose_name=_("buy deadline"))
    year_rate = models.FloatField(verbose_name=_("year rate"))
    commission_sale_leader = models.CharField(verbose_name=_("commission sale leader"), max_length=32)
    commission_team_leader = models.CharField(verbose_name=_("commission team leader"), max_length=32)
    commission_sale_leader_rate = models.FloatField(verbose_name=_("commission sale leader rate"))
    commission_team_leader_rate = models.FloatField(verbose_name=_("commission team leader rate"))
    commission_sale_leader_sum = models.FloatField(verbose_name=_("commission sale leader sum"), null=True)
    commission_team_leader_sum = models.FloatField(verbose_name=_("commission team leader sum"), null=True)
    commission_deadline = models.IntegerField(verbose_name=_("commission deadline"))
    manager = models.CharField(verbose_name=_("manager"), max_length=32)
    
    class Meta:
        verbose_name = _("sale order")
        verbose_name_plural = _("sale orders")
    
class Contract(models.Model):
    number = models.CharField(verbose_name=_("number"), max_length=32)
    into_way = models.CharField(verbose_name=_("into way"), max_length=32)
    project_name = models.ForeignKey(Project, verbose_name=_("project name"))
    seller = models.ForeignKey(Employee, verbose_name=_("seller"))
    customer_name = models.CharField(verbose_name=_("customer name"), max_length=32)
    customer_ID = models.CharField(verbose_name=_("customer ID"), max_length=32)
    bank_name = models.CharField(verbose_name=_("bank name"), max_length=32)
    bank_account = models.CharField(verbose_name=_("bank account"), max_length=32)
    buy_date = models.DateField(verbose_name=_("buy date"))
    buy_sum = models.IntegerField(verbose_name=_("buy sum"))
    buy_category = models.CharField(verbose_name=_("buy category"), max_length=32)
    buy_deadline = models.IntegerField(verbose_name=_("buy deadline"))
    year_rate = models.FloatField(verbose_name=_("year rate"))
    payment_date = models.DateField(verbose_name=_("payment date"), default=datetime.datetime.strftime(datetime.date.today(), "%Y-%m-%d"))

    class Meta:
        verbose_name = _("sale contract")
        verbose_name_plural = _("sale contracts")