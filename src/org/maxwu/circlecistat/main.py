#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import yaml
import os
from org import ROOT_DIR

"""Main script file to provide configuration loading, cli_app and version.
"""

VERSION = "1.0"
CONFIG_YAML = "config.yaml"

def cli_app():
    print "CLI starts"
    pass


def get_cfg():
    # By default, the main module shall search config.yaml in app root dir.
    path = '/'.join([ROOT_DIR, CONFIG_YAML])
    cfg = file(path)
    ycfg = yaml.load(cfg)
    return ycfg


def get_cfg_token():
    return get_cfg()['circleci']['api-token']


if __name__ == '__main__':
    cli_app()

