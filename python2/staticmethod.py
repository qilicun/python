#!/usr/bin/env python

class Test(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print self.data

t1 = Test('arun')
t2 = Test('seema')

t1.printd()
t2.printd()
