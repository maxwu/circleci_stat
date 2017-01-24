#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import unittest
import logging
import sys
from org.maxwu.casual_dev import *

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)


class CasualDevIoTest(unittest.TestCase):
    def setUp(self):
        print "Preparing the logging.."
        # Set logger handler to current stdout stream
        logger.addHandler(stream_handler)

    def test_find_even_number(self):
        even_num_list = find_even_number(8)
        created_even_numbers = range(0, 8, 2)
        print "\n"
        print "even numbers within 8:%s" % even_num_list
        print "created even numbers :%s" % created_even_numbers
        self.assertListEqual(even_num_list, created_even_numbers)

    def test_find_even_number_with_logger(self):
        even_num_list = find_even_number(12)
        logging.getLogger().info("even numbers within 12:%s" % even_num_list)
        created_even_numbers = range(0, 12, 2)
        self.assertListEqual(even_num_list, created_even_numbers)

    def tearDown(self):
        logger.removeHandler(stream_handler)

if __name__ == '__main__':
    unittest.main()

"""
 Note 1: Generally python unittest will not print stdout by default.
    To see the stdout results, nose + "-s" could collect the stdout and print by the end no matter the case passes or not.

 Note 2: For unittest, it is better to use logging module.
    -TBD-
"""

"""
    # Below is to redirect output stream (from stderr by TextTestRunner default) to stdout.
    io_demo_test = unittest.TestLoader().loadTestsFromTestCase(CasualDevIoTest)
    unittest.TextTestRunner(stream=sys.stdout).run(io_demo_test)
"""