#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'


import requests
from requests.auth import HTTPBasicAuth
import json
import main

class CircleCiReq(object):
    """Helper to fetch build artifacts from circleci.com
    https://circleci.com/docs/api/
    GET: /project/:vcs-type/:username/:project
    Build summary for each of the last 30 builds for a single git repo.
    """
    BASE_URL = "https://circleci.com/api/v1.1/"

    @classmethod
    def get_builds(cls, token, vcs, username, project):
        url = cls.BASE_URL + '/'.join(['project', vcs, username, project])
        print 'req url is {0}'.format(url)
        r = requests.get(url, auth=HTTPBasicAuth(token, ''))
        print r.text
        res_json = r.json()
        # print json.dumps(rjson[0], indent = 4)
        # reponame = res_json[0]['reponame']
        # vcs_type = res_json[0]['vcs_type']
        # username = res_json[0]['username']
        return

if __name__ == "__main__":
    CircleCiReq.get_builds(main.get_cfg_token(), 'github', 'maxwu', 'cucumber-java-toy')
    pass

