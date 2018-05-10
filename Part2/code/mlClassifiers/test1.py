# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:40:38 2018

@author: hadoop
"""
from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext

from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

conf = SparkConf().setAppName("NeuralNetworks")
conf = conf.setMaster("local[*]")
sc   = SparkContext(conf=conf)

sqlContext = SQLContext(sc)

# Load training data
data = sqlContext.read.format("libsvm")\
    .load("doc2.txt")

# Split the data into train and test
splits = data.randomSplit([0.6, 0.4],1234)
train = splits[0]
test = splits[1]


train.show()