#!/usr/bin/python3

import time
import pprint

class Tools():
    
    def pretty_print(someObject):
        pp = pprint.PrettyPrinter(indent="4")
        return pp.pprint(someObject)

    
    def pp(someObject):
        Tools.pretty_print(someObject)
        time.sleep(5)