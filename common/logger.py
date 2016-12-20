#!/usr/bin/python
#-*- coding:utf-8 -*-
#author:lwl

import os
import sys
sys.path.append('..')
import logging
import logging.handlers
import logging.config
from .signleton import signleton
from mis.settings import BASE_DIR
from .config import LogCon

@signleton
class log():
    def __init__(self):
        level_config = LogCon.level
        file_name = LogCon.file_name
        log_file = os.path.join(BASE_DIR, 'log', file_name)
        level = level_config.upper()
        level_dict = {'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR,
                      'CRITICAL': logging.CRITICAL,
                      'NOTSET': logging.NOTSET
                     }
        log_level = level_dict.get(level, '')
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)
        handler = logging.handlers.TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=10)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

logger = log().logger
