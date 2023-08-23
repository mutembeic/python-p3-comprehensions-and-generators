#!/usr/bin/env python3

def return_evens(num_list): 
    return [x for x in num_list if x % 2 == 0]
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)
  
     

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)