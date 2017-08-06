#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Captured WebDriver
Selenium WebDriver to capture existing session

"""
from selenium import webdriver as wd
from selenium.webdriver.remote.webdriver import WebDriver


class CapturedDriver(WebDriver):
    """
    >>> CapturedDriver.doctest_visit_github()
    PASS
    """
    def __init__(self,
                 command_executor=None,
                 desired_capabilities={},
                 browser_profile=None,
                 proxy=None,
                 keep_alive=False,
                 session_id=None,
                 w3c=True):
        super(CapturedDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)
        self.session_id = session_id
        self.w3c = w3c

    def start_session(self, desired_capabilities, browser_profile):
        self.capabilities = {}

    @staticmethod
    def doctest_visit_github():
        d = wd.Firefox()
        d.get('http://github.com')
        # "The world's leading software development platform · GitHub"
        title1 = d.title
        d2 = CapturedDriver(command_executor=d.command_executor, session_id=d.session_id, w3c=d.w3c)
        title2 = d2.title
        if title1 == title2:
            print "PASS"
        else:
            print "driver title is %s, captured driver title is %s" % (title1, title2)
        d.quit()

if __name__ == "__main__":
    import doctest
    doctest.testmod()


