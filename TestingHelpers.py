#!/usr/bin/python3

import pprint

class TestingHelpers():
    
    def pp(object):
        pp = pprint.PrettyPrinter(indent="4")
        return pp.pprint(object)

