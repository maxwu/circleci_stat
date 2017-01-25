#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

from contextlib import contextmanager
from StringIO import StringIO
import sys
import unittest


@contextmanager
def capture_output():
    new_stdout, new_stderr = StringIO(), StringIO
    old_stdout, old_stderr = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_stdout, new_stderr
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr


class OutPrintTest(unittest.TestCase):
    def output_test(self):
        # "as" -> (out, err) = capture_output()
        # and decorate the block with given __enter__()/__exit__()
        with capture_output() as (out, err):
            print "This is a test"

        output = out.getvalue().strip()
        self.assertEqual(output, 'This is a test')
        print 'The captured results are: "%s"' %(output)


if __name__ == '__main__':
    unittest.main()