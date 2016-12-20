# coding=utf-8

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyAppConfig(AppConfig):
    name = 'team'
    verbose_name = _("sale team")