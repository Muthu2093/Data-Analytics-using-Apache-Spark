#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:24:54 2018

@author: muthuvel
"""
from nytimesarticle import articleAPI
api = articleAPI('fa567ce571174336957fc6786b4dc91e')

articles = api.search( q = 'soccer', 
     fq = {'Title':'Sports', 'source':['Reuters','AP', 'The New York Times']}, 
     begin_date = 20111231 )