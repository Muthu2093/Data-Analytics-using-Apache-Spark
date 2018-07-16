# Document Classification System using Apache Spark

Built various Machine Learning Classfiers in pyspark for identifying/ classifying article from web, with respect to their category. The model is trained in pyspark with a dataset collected from New York Times using NYTimes API in Python. Map Reduce framework is employed for extracting features in from the dataset

## Getting Started

Clone the repository and run the scripts from part2/mlClassifers in pyspark to test the implementation

### Prerequisites

The model requires the following modules to work 

```
Apache Spark
```

```
Python3
```


```
NYTimes API
```

### Installing

Follow the link below to install pyspark libraries

```
https://github.com/KristianHolsheimer/pyspark-setup-guide
```
To install  nytimesarticle API follow instruction in
```
https://github.com/MattDMo/NYTimesArticleAPI
```

## Running the tests

The project can be tested in three parts

### Collecting articles

Goto part2/code/dataCollection/ and run the below command

```
python nyTimesArticlesExtraction.py
```
Change the API setting in the script as per the requirements

###  Feature Extraction

Goto part2/code/featureExtraction/ in pyspark and run the below command

```
spark submit featureExtraction.py
```
NOTE: This steps require pyspark to be already installed

###  Testing the Classifers

Goto part2/code/mlClassifiers/ in pyspark and run the below command

```
spark submit ******.py
```
NOTE: Replace "******" with the name of the pyspark classifier present in the directory

Current implementation uses,
* Decision Trees
* Logistic Regression
* Naive Bayes
* Neural Network
* Random Forests


## Authors

* **Muthuvel Palanisamy** - *Initial work* - [muthu2093](https://github.com/muthu2093)
* **Akshay Chopra** - *Initial work* - [askshay993](https://github.com/akshay993)

See also the list of [contributors](https://github.com/Muthu2093/Data-Analytics-using-Apache-Spark/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


