from pyspark.ml.classification import LogisticRegression

from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("NeuralNetworks")
conf = conf.setMaster("local[*]")
sc   = SparkContext(conf=conf)

sqlContext = SQLContext(sc)

# Load training data

df = sqlContext.read.format("com.databricks.spark.csv").option("delimiter", "\t").option("header", "true").load("doc3.txt")

(trainingData, testData) = df.randomSplit([0.7, 0.3])

# Load training data
training = sqlContext \
    .read \
    .format("libsvm") \
    .load("doc3.txt")

lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

training.show()
# Fit the model
lrModel = lr.fit(training)

# Print the coefficients and intercept for multinomial logistic regression
print("Coefficients: \n" + str(lrModel.coefficientMatrix))
print("Intercept: " + str(lrModel.interceptVector))


# We can also use the multinomial family for binary classification
mlr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family="multinomial")

# Fit the model
mlrModel = mlr.fit(training)

# Print the coefficients and intercepts for logistic regression with multinomial family
print("Multinomial coefficients: " + str(mlrModel.coefficientMatrix))
print("Multinomial intercepts: " + str(mlrModel.interceptVector))
    # $example off$