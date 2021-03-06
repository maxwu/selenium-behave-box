#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Captured WebDriver
Selenium WebDriver to capture existing session
"""
from selenium import webdriver as wd
from selenium.webdriver.remote.webdriver import WebDriver
import os
import requests
import json

# for doctest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class CapturedDriver(WebDriver):
    """
    >>> doctest_ff_headless_visit_github()
    PASS
    >>> doctest_ff_visit_github()
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
        self.capabilities = desired_capabilities
        self.w3c = w3c

    def start_session(self, desired_capabilities, browser_profile):
        self.capabilities = {}

    # return tuple of session ID and capabilities dict.
    @staticmethod
    def get_session_id_and_capabilities(command_executor=None):
        if not command_executor:
            return None

        # requests respects environment variables on proxy and does not bypass localhost.
        # It seems the recent IETF draft catches eyes to solve such issues,
        # https://tools.ietf.org/html/draft-west-let-localhost-be-localhost-04
        os.environ['NO_PROXY'] = 'localhost'

        url = command_executor + '/sessions'
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        if data['value']:
            return data['value'][0]['id'], data['value'][0]['capabilities']
        else:
            return None


# doctest on web driver title.
def doctest_ff_visit_github():
    binary = FirefoxBinary('/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox')
    d = wd.Firefox(firefox_binary=binary)
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


# doctest on web driver title with headless FF
# For headless FF, either MOZ_HEADLESS environment or -headless option specified in binary command.
def doctest_ff_headless_visit_github():
    os.environ['MOZ_HEADLESS'] = '1'
    binary = FirefoxBinary('/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox')
    d = wd.Firefox(firefox_binary=binary)

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
    del os.environ['MOZ_HEADLESS']

if __name__ == "__main__":
    import doctest
    doctest.testmod()


