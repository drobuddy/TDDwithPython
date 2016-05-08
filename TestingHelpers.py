#!/usr/bin/python3

import pprint

class Tools():
    
    def pp(someObject):
        pp = pprint.PrettyPrinter(indent="4")
        return pp.pprint(someObject)

