from __future__ import print_function

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from operator import add

#import pyspark

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import IntegerType
from pyspark.sql import Row # for DF creation
from pyspark.sql import SQLContext # for DF
from pyspark.ml.feature import StopWordsRemover ##for stop words removal


stop_words=["mr.","said","said","how","said,","because","do","there",
"make","now","its","two","one","said.","chief","up","if","out","some",
"what","just","year","like","told","since","only","may","into","any","one",
"over","after","three","before","him","them","back","four","did","get","-",
"mr","most","no","other","also","much","so","many","could","last","all",
"new","percent","than","can","her","about","would","said","more","has",
"or","i","are","will","but","it","its","be","been","at","said","his",
"have","by","had","from","not","at","as","the","with","of","a", "an", 
"the", "this", "that","those", "on", "in", "for","he", "she","their", 
"they", "we","been", "i", "you", "who", "which", "where", "when", "why", 
"was", "were","while","under","my","me", "is", "hi" , "hey", "hello","to",
"and","got","former","against","mrs.","mrs","between","ms.","ms","first",
"second","third","fourth","people","even","still","each"]



def read_directory(sc, path):
    icount=0;
    
    feature_list=[]
    textRDD=sc.textFile(path)
    words = textRDD.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1))
    wordcount = words.reduceByKey(add).map(lambda (x,y): (y,x)).sortByKey(ascending=False).collect()
    
    #CONVERSION TO DF
    R = Row('count', 'words')
    sqlContext = SQLContext(sc)
    DF = sqlContext.createDataFrame([R(i, x) for i, x in (wordcount)])
    DF.show()
    
    #mvv_list = DF.select('words').show()
    
    for (count, word) in wordcount:
        
        try:
            mynewstring = word.encode('ascii')
        except:
            #print("there are non-ascii characters in there")
            continue    
        
        if word.lower() in stop_words:
            continue
        else:
            print("%s: %i" % (word, count))
            if(icount!=50):
                feature_list.append(word)
                icount=icount+1
            else:
                break                      
    
    return feature_list

if __name__ == "__main__":
    
    conf = SparkConf().setAppName("Lab3")
    conf=conf.setMaster("local[*]")
    sc=SparkContext(conf=conf)
    path="../../data/Health/*.txt"
    
    
    bs_list= read_directory(sc,path)
    
    for word in bs_list:
        print("%s: " % (word))



	