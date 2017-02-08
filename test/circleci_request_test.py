#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import unittest
from me.maxwu.circlecistat.circleci_request import CircleCiReq
from me.maxwu.circlecistat import main


class CircleCiReqTest(unittest.TestCase):
    def test_30builds(self):
        builds = CircleCiReq.get_recent_30builds(token=main.get_cfg_token(), vcs='github', username='maxwu', project='cucumber-java-toy')
        self.assertEqual(30, len(builds))

    def test_30artifacts(self):
        builds = CircleCiReq.get_recent_30artifacts(token=main.get_cfg_token(), vcs='github', username='maxwu', project='cucumber-java-toy')
        print "numbers are {0}".format(builds)
        self.assertEqual(30, len(builds))


if __name__ == '__main__':
    unittest.main()
