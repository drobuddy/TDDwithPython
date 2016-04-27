#!/usr/bin/python3

import pprint

class TestingHelpers():
    
    def pp(object):
        pp = pprint.PrettyPrinter(indent="4")
        pp.pprint(object)
        return False

