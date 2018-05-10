#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 11:04:22 2018

@author: muthuvel
"""

import codecs
try:
    f = codecs.open("/Users/muthuvel/Documents/GitHub/Data-Analytics-using-Apache-Spark/Part2/data/Health/0.txt", encoding='utf-8', errors='strict')
    for line in f:
        pass
    print ("Valid utf-8")
except UnicodeDecodeError:
    print ("invalid utf-8")