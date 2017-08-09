#!/usr/bin/env python
# -*- coding: utf-8 -*-

from capdriver.captured_driver import CapturedDriver

if __name__ == "__main__":
    d = CapturedDriver(command_executor='http://localhost:6064 ', session_id='49075f494d1add687ab74f1cb95f0314')
    print "Captured Session Title is %s" % d.title
    explore = d.find_element_by_link_text("Explore")
    explore.click()
    print "Captured Session Title changes to %s" % d.title
    d.back()
