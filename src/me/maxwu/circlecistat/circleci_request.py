#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'


import requests
from requests.auth import HTTPBasicAuth
import logging
import json


logging.basicConfig(format = '%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CircleCiReq(object):
    """Helper to fetch build artifacts from circleci.com
    https://circleci.com/docs/api/
    GET: /project/:vcs-type/:username/:project
    Build summary for each of the last 30 builds for a single git repo.
    """
    BASE_URL = "https://circleci.com/api/v1.1/"

    @classmethod
    def get_artifacts(cls, token, vcs, username, project, build_num):
        """
        Get a list of artifacts generated with given build number
        """
        build_num = str(build_num)
        url = cls.BASE_URL + '/'.join(['project', vcs, username, project, build_num, 'artifacts'])
        logger.info('req url is {0}'.format(url))

        r = requests.get(url, auth=HTTPBasicAuth(token, ''))
        logger.debug("result is:\n{0}".format(r.text))
        json_res = r.json()

        for artifact in json_res:
            yield artifact['url']

    @classmethod
    def get_recent_30builds(cls, token, vcs, username, project):
        url = cls.BASE_URL + '/'.join(['project', vcs, username, project])
        logger.info('req url is {0}'.format(url))

        r = requests.get(url, auth=HTTPBasicAuth(token, ''))
        # FIXME: add status code check
        # FIXME: add log

        res_json = r.json()
        for index, build in enumerate(res_json):
            logger.debug("number {} \n {}\n".format(index, json.dumps(build, indent=2)))
            yield build

    @classmethod
    def get_recent_30artifacts(cls, token, vcs, username, project):
        builds = cls.get_recent_30builds(token=token, vcs=vcs, username=username, project=project)
        build_nums = [build['build_num'] for build in builds]

        for num in build_nums:
            yield cls.get_artifacts(token=token,
                                  vcs=vcs,
                                  username=username,
                                  project=project,
                                  build_num=num,
                                  )


if __name__ == "__main__":
    pass

