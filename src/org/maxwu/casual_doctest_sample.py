#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'

import sys


def casual_find_pos_with_iter(n, from_list):
    """Return the element position in list or None.
        >>> casual_find_pos_with_iter(2, [0,1,2,3,4,5])
        2
        >>> casual_find_pos_with_iter(5, [0,1,2,3,4,5])
        5
        >>> casual_find_pos_with_iter(2, range(6))
        2
        >>> casual_find_pos_with_iter(7, range(6))
    """
    return next(iter([x for x in from_list if x == n]), None)


def casual_find_pos_with_gen(n, from_list):
    """Return the element position in list or None.
    :param n: target element eligible "==" operator.
    :param from_list: list to look up
    :return: position, or, None

    >>> casual_find_pos_with_gen(2, range(6))
    2
    >>> casual_find_pos_with_gen(0, range(7))
    0
    >>> casual_find_pos_with_gen(7, range(6))
    """
    return next((x for x in from_list if x == n), None)


def casual_find_pos_with_bin(n, from_list):
    """Return the element position in **sorted** list or None.
    :param n: target element eligible "==" operator.
    :param from_list: **sorted** list to look up
    :return: position, or, None
    === Doc Test ===
    >>> casual_find_pos_with_bin(8, [x*2 for x in range(10)])
    4
    >>> casual_find_pos_with_bin(0, range(7))
    0
    >>> casual_find_pos_with_bin(6, range(7))
    6
    >>> casual_find_pos_with_bin(7, range(6))
    >>> casual_find_pos_with_bin(0, range(1,6))
    >>> casual_find_pos_with_bin(8, [x*2+1 for x in range(6)])
    >>> casual_find_pos_with_bin(4, [1,2,3,3,4,4,6])
    5
    """
    start = 0
    end = len(from_list) - 1
    found = False

    while end >= start and not found:
        mid = (start + end) / 2
        sys.stderr.write("n=%d, start=%d, end=%d, mid=%d, list=%s\n"%(n, start, end, mid, from_list))
        sys.stderr.flush()
        if n == from_list[mid]:
            found = True
        elif n < from_list[mid]:
            end = mid-1
        else:
            start = mid + 1

    if found:
        return mid
    else:
        return None

if __name__ == "__main__":
    print ">" * 80
    # Start doctest
    import doctest
    doctest.testmod(verbose=True)