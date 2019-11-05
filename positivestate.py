# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:38:53 2016

@author: a_danda
"""


import json
import re
import operator
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
  
"""print scores.items() # Print every (term, score) pair in the dictionary"""

statesfile = open("states.txt")
states = []
for line in statesfile:
    pattern = re.compile("^\s+|\s*,\s*|\s+$")
    states.append(pattern.split(line))
#print states
states =[item for sublist in states for item in sublist]
states = [x.lower() for x in states]

value = 0
word_list = []
tweetscore_list = {}
for dict_n in data:
        key =  dict_n.keys()
        if len(key) > 1:
            
            key1 = key[2]
            tweet = dict_n[key1] 
            tweet = tweet.lower()
            word_list = re.findall(r'\w+', tweet ,flags = re.UNICODE | re.LOCALE)
           
            
            #print word_list
            for word in word_list:
                #print word
                if word.encode('utf-8') in scores.keys():
                  #print word  
                  value = value+scores[word]
                  #print value   
            for state in states:
                if state in word_list:
                    #print "1"
                    tweetscore_list[state] =  value
            #print tweetscore_list        
            value = 0    
            word_list = []
#print tweetscore_list
print max(tweetscore_list.iteritems(), key=operator.itemgetter(1))[0]
