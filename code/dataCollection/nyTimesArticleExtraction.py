#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:24:54 2018

@author: muthuvel
"""
from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import urllib

# Define API key and query term
api = articleAPI('fa567ce571174336957fc6786b4dc91e')
category = 'Politics'
search_keyword = "trump"
##Keywords used so far
# Politics - trump, democracy, Republicans, Democrats
# Method to extract the content of the url
def parseURL(url):
    g = urllib.request.urlopen(url)
    soup = BeautifulSoup(g.read(), 'html.parser')
    # Article = soup.find(id='story') - denoted only the content
    
    # Classes that containg the main contents of the articles
    mydivs = soup.findAll("p", {"class": "css-imjp5j e2kc3sl0"})
    
    # For articles in which  the above class extraction command fails
    if (mydivs == []):
        mydivs = soup.findAll("p", {"class": "story-body-text story-content"})
    
    if (mydivs == []):
        return []
    
    # Adding title to the content
    content = soup.title.text
    for j in range(0,len(mydivs)):
        content = content + '\n' + mydivs[j].text 
    
    return content
        

# Main code begins
if __name__ == "__main__":
    print('File loaded directly')
    articles = api.search(q=search_keyword, begin_date = 20081231, page=3)
    response = articles['response']
    docs = response['docs']
    
    # Index contains the metadata - url of all the articles collected so far
    index = open("../../data/%s/metadata/index.txt" %(category),"r")
    
    # Creating an index file if this the first time articles are collected on a topic
    if (index.readlines() == []):
        index = open("../../data/%s/metadata/index.txt" %(category),"w+")
        web_url=[]
        for i in range(0,len(docs)):
            web_url.append(docs[i]['web_url'])
            index.writelines("%s\n" % docs[i]['web_url'])
    index.close()  
    
    # Reading index file
    index = open("../../data/%s/metadata/index.txt" %(category),"r")
    web_url = index.read()
    web_url = web_url.splitlines()
    
    # Appending all collected articles to the existing URLs and saving to the index file
    for i in range(0,len(docs)):
        web_url.append(docs[i]['web_url'])  
    web_url = list(set(web_url))    #removes duplicates
    index = open("../../data/%s/metadata/index.txt" %(category),"w+")
    for i in range(0,len(web_url)):
            index.writelines("%s\n" % web_url[i])
    index.close()  
        
    # Extract contents of url one by one and write it to text file
    for i in range(0,len(web_url)):
        Article_content = parseURL(web_url[i])
        if (Article_content == []):
            continue
        f = open("../../data/%s/%s.txt" %(category, i),"w+")
        f.write(Article_content)
        f.close()
        #index = index + 1
    
    #index.write(str())
    #index.close()