#!/usr/bin/env python

import ConfigParser

parser = ConfigParser.ConfigParser()
parser.read("config.ini")
name = parser.get("info", "name")
sex = parser.get("info", "sex")
age = parser.getint("info", "age")

height = parser.get("data", "height")
weight = parser.get("data", "weight")

print type(age)
print name, sex, age, height, weight
