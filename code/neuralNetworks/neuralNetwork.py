#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 05:29:48 2018

@author: muthuvel
"""

import tensorflow as tf
import numpy as np
from scipy.optimize import minimize
from scipy.io import loadmat
from math import sqrt
import math
from sklearn.feature_selection import VarianceThreshold
import timeit
import pickle

m = loadmat('mnist_all.mat')
