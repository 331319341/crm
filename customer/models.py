from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from common import const

#from . import Gender

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=32)
    
class Gender(models.Model):
    title = models.CharField(max_length=32)
    
class Project(models.Model):
    title = models.CharField(max_length=32)

class Customer(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=32)
    birth = models.DateField()
    gender = models.CharField(_("gender"),max_length=const.DB_CHAR_CODE_2,choices=const.get_value_list('gender'),default='1')
    addr = models.CharField(max_length=32)
    phone = models.IntegerField()
    email = models.CharField(max_length=32)
    qq = models.IntegerField()
    shoumairen = models.ForeignKey(User)
    beizhu = models.CharField(max_length=256)
    
class xiaoshou(models.Model):
    customer = models.ForeignKey(Customer)
    amount = models.IntegerField()
    unit = models.CharField(max_length=8, choices=const.get_unit_list(),default='1')
    xiaoshou = models.ForeignKey(User)
    start_time = models.DateField()
    end_time = models.DateField()
    beizhu = models.CharField(max_length=256)