# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'maxwu'

"""Casual module for development experiments
    This module is reserved for experiment codes and internal test.
    It is not expected to launch official test on this module.
"""
import string

def casual_func(n=1):
    return n + 1


def find_even_number(n=10):
    return [i for i in range(n) if i % 2 == 0]


def print_directory_contents(path):
    # Recursively list the contents under path
    import os
    for sub_node in os.listdir(path):
        sub_node_path = os.path.join(path, sub_node)
        if os.path.isdir(sub_node_path):
            print_directory_contents(sub_node_path)
        else:
            print ">>> %s" %(sub_node_path)
    return


def casual_zip(n=5):
    numbers = range(n)
    letters = string.ascii_lowercase[:n]
    letters_cap = string.ascii_uppercase[:n]
    combined = zip(numbers, letters)  # aligned up with the shorter list.
    combined_dict = dict(combined)
    numbers.remove(0)                               # list is immutable, list.remove() just return None
    combined_trunc1 = zip(numbers, letters)         # the extra elements are dropped.
    numbers.append(n)
    combined_trunc2 = zip(numbers, letters[1:])     # string is immutable, too. But slice() return new object.

    print numbers
    print letters
    print "typeof string.ascii_lowercase:%s" %(type(string.ascii_lowercase))
    print "typeof list:%s" % (type(list(string.ascii_lowercase)))
    print "combined:%s" %(combined)
    print "combined_dict:%s" % (combined_dict)
    print "combined_trunc1:%s" % combined_trunc1
    print "combined_trunc2:%s" % combined_trunc2

    print "-"*80
    a2 = sorted([i for i in range(10) if i in combined_dict])
    print "a2 = %s" %a2


def casual_list():
    # range(10) builds list 0 to 9 = range(0, 10) = [0,10)
    # In Py3, it returns class range and behaves same as xrange()
    print "range(10):%s" %(range(10))


if __name__ == "__main__":
    print "starting the casual dev checks..."
    print "casual_func(2)=" + str(casual_func(2))
    print "even number within 20:%s" % ",".join([str(i) for i in find_even_number(20)])
    print_directory_contents(".")
    casual_zip(6)
    casual_list()
    print "{:.1%}".format(2.0/149)


# EOF
