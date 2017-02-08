#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import yaml
import os
from me import ROOT_DIR

"""Main script file to provide configuration loading, cli_app and version.
"""

VERSION = "1.0"
CONFIG_YAML = "config.yaml"

def cli_app():
    print "CLI starts: Not implemented cli_app()"
    pass


def get_cfg():
    # By default, the main module shall search config.yaml in app root dir.
    path = '/'.join([ROOT_DIR, CONFIG_YAML])
    cfg = file(path)
    ycfg = yaml.load(cfg)
    return ycfg


# FIXME: Considering a general env filter to figure out all "circleci_" prefixed environmental variables.
def get_cfg_token():
    if os.environ.has_key('circleci_api_token'):
        value = os.environ['circleci_api_token']
    else:
        value = get_cfg()['circleci']['api_token']
    return value


if __name__ == '__main__':
    cli_app()

