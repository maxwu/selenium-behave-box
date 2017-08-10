#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Demo for parametrized test.
Java parametrized sample is located at https://github.com/maxwu/minnetonka/tree/master/src/main/java/sample.
These samples will be merged to a new separate repo.
"""

from parameterized import parameterized
from nose.tools import assert_equal
import unittest


def get_parameters():
    # return list of list
    return [
        ("alpha", "a", "a"),
        ("beta", "a", "b"),
        ("gamma", "b", "b"),
    ]


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ("alpha", "a", "a"),
        ("beta", "a", "b"),
        ("gamma", "b", "b"),
    ])
    def test_sequence(self, name, a, b):
        print "testing %s with (%s, %s)" %(name, a, b)
        assert_equal(a, b)


# if __name__ == "__main__":
#     import nose
#     import sys
#     sys.argv += ['--with-xunit', '--with-html']
#     nose.run()
