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
    >>> casual_find_pos_with_bin(7, range(6)) is None
    True
    >>> casual_find_pos_with_bin(0, range(1,6)) is None
    True
    >>> casual_find_pos_with_bin(8, [x*2+1 for x in range(6)]) is None
    True
    >>> casual_find_pos_with_bin(4, [1,2,3,3,4,4,6])
    5
    """
    start = 0
    end = len(from_list) - 1
    found = False

    # k1: The condition is end>=start;
    # k2: Slice is [begin..mid-1] or [mid+1,end]
    while end >= start and not found:
        mid = (start + end) / 2
        # sys.stderr.write("n=%d, start=%d, end=%d, mid=%d, list=%s\n"%(n, start, end, mid, from_list))
        # sys.stderr.flush()
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


# *params package up parameters into a tuple
# If a list is present, call with casual_sum_param(*in_list)
# While in the def, "*," is used to separate variable params and named parameters
# named keywords could be variable with filler **kw as a dict
# Therefore, the universe sigature could be def func(*args, **kw)
def causal_sum_param(*params):
    total = 0
    for n in params:
        total = total + n
    return total


# FlyWeight with functor, here defines @flyweight for classes.
def flyweight(cls):
    instances = dict()
    return lambda *args, **kargs: instances.setdefault(
                                            (args, tuple(kargs.items())),
                                            cls(*args, **kargs))


def casual_fibonacci_inf():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


def fibonacci_sub(start, end):
    for cur in casual_fibonacci_inf():
        if cur > end:
            return
        if cur >= start:
            yield cur


def fibonacci_num(n):
    res = []
    for index, fib_num in enumerate(casual_fibonacci_inf()):
        print "%d: %d" %(index, fib_num)
        res.append(fib_num)
        if index >= n:
            return res

if __name__ == "__main__":
    print ">" * 80
    # Start doctest
    import doctest
    doctest.testmod(verbose=True)
    print ">" * 80
    print list(fibonacci_sub(0,5))
    print fibonacci_num(10)
