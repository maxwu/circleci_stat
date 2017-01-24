#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import unittest

from org.maxwu.casual_dev import *


class CasualDevTest(unittest.TestCase):
    def test_casual_func(self):
        x = casual_func(2)
        self.assertEqual(3, x, "Wrong func return value")


if __name__ == '__main__':
    unittest.main()
