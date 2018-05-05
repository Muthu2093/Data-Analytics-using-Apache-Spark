from __future__ import print_function

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from operator import add

#import pyspark

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

stop_words=["percent","than","can","her","about","would","said","more","has","or","i","are","will","but","it","be","at","said","his","have","by","had","from","not","at","as","The","with","of","a", "an", "the", "this", "that","those", "on", "in", "for","he", "she","their", "they", "we", "I", "you", "who", "which", "where", "when", "why", "was", "were","while","under","my","me", "is", "hi" , "hey", "hello","to","and"]



def read_directory(sc, path):
    icount=0;
    
    feature_list=[]
    textRDD=sc.textFile(path)
    words = textRDD.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1))
    wordcount = words.reduceByKey(add).map(lambda (x,y): (y,x)).sortByKey(ascending=False).collect()
    
    
    for (count, word) in wordcount:
                    
        if word.lower() in stop_words:
            pass
        else:
            print("%s: %i" % (word, count))
            if(icount!=10):
                feature_list.append(word)
                icount=icount+1
            else:
                break            
                       
    return feature_list

if __name__ == "__main__":
    
    conf = SparkConf().setAppName("Lab3")
    conf=conf.setMaster("local[*]")
    sc=SparkContext(conf=conf)
    path="/home/hadoop/spark/data_lab3/data/Business/*.txt"
    
    
    bs_list= read_directory(sc,path)
    
    for word in bs_list:
        print("%s: " % (word))



	