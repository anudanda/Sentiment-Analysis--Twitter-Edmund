# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 11:57:32 2016

@author: a_danda
"""

import json
import re
import sys
import operator
from pprint import pprint



data = []
with open(sys.argv[1]) as f:
    for line in f:
        data.append(json.loads(line))
#pprint(data)

    
#afinnfile = open(sys.argv[1])
#scores = {} # initialize an empty dictionary
#for line in afinnfile:
 # term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  #scores[term] = int(score)  # Convert the score to an integer.
  
#print scores.items() # Print every (term, score) pair in the dictionary




dtext_list = {}
value = 0
word_list = []
for dict_n in data:
        key =  dict_n.keys()
        if len(key) > 1:
            
            key1 = key[10]
            tweet = dict_n[key1]
            if tweet is not None:
                if 'hashtags' in tweet:
                    tweet1 = tweet['hashtags']
                    #print tweet1
                    for d in tweet1:
                        
                        if 'text' in d:
                            tweet2 = d['text']
                            #print tweet2
                            
                            if not tweet2.encode('utf-8') in dtext_list:
                                dtext_list[tweet2.encode('utf-8')] = 1
                                #print 'entered'
                            else:
                                dtext_list[tweet2.encode('utf-8')] += 1
#print dtext_list                       
            #word_list = re.findall(r'\w+', tweet ,flags = re.UNICODE | re.LOCALE)
            
            
top_ten = list(sorted(dtext_list.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])          
for key, val in top_ten:
    print  " ".join([key, str(val)])

                    
                    
                    
                    
                    


