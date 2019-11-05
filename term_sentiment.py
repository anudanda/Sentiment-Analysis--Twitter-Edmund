# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:40:53 2016

@author: a_danda
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:41:18 2016

@author: a_danda
"""
import json
import re
from pprint import pprint
import sys


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



term_list = {}
value = 0
new_word_list = []
word_list = []
for dict_n in data:
        key =  dict_n.keys()
        if len(key) > 1:
            
            key1 = key[2]
            tweet = dict_n[key1]
            
            tweet = tweet.lower()
            word_list = re.findall(r'\w+', tweet ,flags = re.UNICODE | re.LOCALE) 
            for word in word_list:
               
               if word.encode('utf-8') in scores.keys():
                    
                    index_word = word_list.index(word)
                    if index_word == 1 and len(word_list) == 2:
                        new_word_list = list(word_list[index_word])
                        new_word_list.append(word_list[index_word-1])
                    elif index_word == 0:
                        new_word_list = list(word_list[index_word])
                    elif index_word == 1 and len(word_list) == 3 :
                        new_word_list = list(word_list[index_word])
                        new_word_list.append(word_list[index_word -1])
                        new_word_list.append(word_list[index_word + 1])
                    elif index_word == 1 and len(word_list) > 3 :
                        new_word_list = list(word_list[index_word])
                        new_word_list.append(word_list[index_word -1])
                        new_word_list.append(word_list[index_word + 1])
                        new_word_list.append(word_list[index_word + 2])
                    elif index_word == 2 and len(word_list) == 3 :
                        new_word_list = list(word_list[index_word])
                        new_word_list.append(word_list[index_word -2])
                        new_word_list.append(word_list[index_word - 1])
                    elif index_word == 2 and len(word_list) == 4 :
                        new_word_list = list(word_list[index_word])
                        new_word_list.append(word_list[index_word -2])
                        new_word_list.append(word_list[index_word - 1])
                        new_word_list.append(word_list[index_word + 1]) 
                    elif index_word == 2 and len(word_list) > 4 :
                        new_word_list = list(word_list[index_word])
                        new_word_list.append(word_list[index_word -2])
                        new_word_list.append(word_list[index_word - 1])
                        new_word_list.append(word_list[index_word + 1])
                        new_word_list.append(word_list[index_word + 2])
                    for new_words in new_word_list:
                             if new_words.encode('utf-8') in scores.keys():
                                 value = value+scores[new_words]
                             else:
                                 "not in scores"
               
               if word not in term_list:      
                   term_list[word] = value
               else:
                   term_list[word] = term_list[word] + value
                   value = 0
        else:
            "length less than 1"
            

for key, val in term_list.items():
    print " ".join([key, str(val)])
