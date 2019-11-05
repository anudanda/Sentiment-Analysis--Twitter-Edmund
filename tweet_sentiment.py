# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 11:57:32 2016

@author: a_danda
"""



import json
import re
import sys
from pprint import pprint





data = []
with open(sys.argv[2]) as f:
    for line in f:
        data.append(json.loads(line))
#pprint(data)

    
afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.
  
#print scores.items() # Print every (term, score) pair in the dictionary
      



value = 0
word_list = []
tweetscore_list = []
for dict_n in data:
        key =  dict_n.keys()
        if len(key) > 1:
            
            key1 = key[2]
            
            tweet = dict_n[key1]
            if tweet is not None:
                tweet = tweet.lower()
                word_list = re.findall(r'\w+', tweet ,flags = re.UNICODE | re.LOCALE) 
            
            
                """print word_list"""
                for word in word_list:
                
                    if word.encode('utf-8') in scores.keys():
                        #print word  
                        value = value+scores[word]
                
                        return(value)
                value = 0    
        
#print tweetscore_list
