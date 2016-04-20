#encoding=utf8

import log4py

def getLogger(name):
    log = log4py.Logger().get_instance(name)
    return log
