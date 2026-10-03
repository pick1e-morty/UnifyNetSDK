# -*- coding: utf-8 -*-
"""厂商配置注册表。新增厂商只需加一个 config/<sdk>.py 并在这里登记。"""
from .dahua import DAHUA
from .haikang import HAIKANG

CONFIGS = {'dahua': DAHUA, 'haikang': HAIKANG}


def get_config(name):
    return CONFIGS[name]
