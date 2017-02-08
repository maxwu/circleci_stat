#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'


import requests
from requests.auth import HTTPBasicAuth
import json


class CircleCiReq(object):
    """Helper to fetch build artifacts from circleci.com
    https://circleci.com/docs/api/
    GET: /project/:vcs-type/:username/:project
    Build summary for each of the last 30 builds for a single git repo.
    """
    BASE_URL = "https://circleci.com/api/v1.1/"

    @classmethod
    def get_recent_30builds(cls, token, vcs, username, project):
        url = cls.BASE_URL + '/'.join(['project', vcs, username, project])
        print 'req url is {0}'.format(url)
        # FIXME: add log

        r = requests.get(url, auth=HTTPBasicAuth(token, ''))
        # FIXME: add status code check
        # FIXME: add log

        """
        Each one is a json in json list [].
{
  "vcs_revision" : "73b470133596aa77715290f613808647d9eda8b9",
  "vcs_tag" : null,
  "build_num" : 51,
  "infrastructure_fail" : false,
  "committer_email" : "maxwunj@gmail.com",
  "previous" : {
    "build_num" : 50,
    "status" : "canceled",
    "build_time_millis" : 592484
  },
  "status" : "timedout",
  "committer_name" : "maxwu",
  "retries" : null,
  "subject" : "Remove synch from DriverFactory",
  "vcs_type" : "github",
  "timedout" : true,
  "dont_build" : null,
  "lifecycle" : "finished",
  "no_dependency_cache" : true,
  "stop_time" : "2017-01-13T00:08:39.539Z",
  "ssh_disabled" : false,
  "build_time_millis" : 770258,
  "circle_yml" : {
    "string" : "machine:\n  java:\n    version: oraclejdk8\ntest:\n  post:\n    - mkdir -p $CIRCLE_TEST_REPORTS/junit/\n    - find . -type f -regex \".*/target/surefire-reports/.*xml\" -exec cp {} $CIRCLE_TEST_REPORTS/junit/ \\;\n"
  },
  "messages" : [ ],
  "is_first_green_build" : false,
  "job_name" : null,
  "start_time" : "2017-01-12T23:55:49.281Z",
  "canceler" : null,
  "all_commit_details" : [ {
    "committer_date" : "2017-01-13T12:35:16+13:00",
    "body" : "",
    "branch" : "dev",
    "author_date" : "2017-01-13T12:35:16+13:00",
    "committer_email" : "maxwunj@gmail.com",
    "commit" : "73b470133596aa77715290f613808647d9eda8b9",
    "committer_login" : "maxwu",
    "committer_name" : "maxwu",
    "subject" : "Remove synch from DriverFactory",
    "commit_url" : "https://github.com/maxwu/cucumber-java-toy/commit/73b470133596aa77715290f613808647d9eda8b9",
    "author_login" : "maxwu",
    "author_name" : "maxwu",
    "author_email" : "maxwunj@gmail.com"
  } ],
  "outcome" : "timedout",
  "vcs_url" : "https://github.com/maxwu/cucumber-java-toy",
  "author_name" : "maxwu",
  "node" : null,
  "queued_at" : "2017-01-12T23:55:49.258Z",
  "canceled" : false,
  "author_email" : "maxwunj@gmail.com"
}
        """

        res_json = r.json()
        for index, artifact in enumerate(res_json):
            print "number {} \n {}\n".format(index, json.dumps(artifact, indent=2))
        # FIXME: change to log

        return res_json

    @classmethod
    def get_recent_30artifacts(cls, token, vcs, username, project):
        builds = cls.get_recent_30builds(token=token, vcs=vcs, username=username, project=project)
        build_nums = [build['build_num'] for build in builds]
        return build_nums

if __name__ == "__main__":
    pass

