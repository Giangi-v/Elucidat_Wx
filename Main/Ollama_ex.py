#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:42:40 2025

@author: elucidatspare
"""

# imports 

from ollama import chat
from ollama import ChatResponse
from ollama import pull
from ollama import list as ollama_list

import sqlite3


def get_model_list():
    model_list_raw = str(ollama_list())
    
    found = True
    model_list = []
    
    while found == True: 
        # find location of model name
        index_start = model_list_raw.find('(model=') + 8
        index_end = model_list_raw.find(', modified_at') - 1
        
        # add model name to list
        model_list.append(model_list_raw[index_start:index_end])
        
        # remove leading model name
        model_list_raw = model_list_raw[index_end+14:]
        
        # check loop condition
        try:
            index_test = model_list_raw.index('(model=')  
        except:
            found = False
              
    return model_list
  
      
def model_pull(model_name): #pull model to device
    pull(model_name)    


def call_and_respond(modelName, input_string):
    response: ChatResponse = chat(model=modelName, messages=[
        {
            'role': 'user',
            'content': input_string,
            },
        ])
    #print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
    return response.message.content
    
    


#define model
model_name = 'smollm:latest' #'wizardlm2' #'tinyllama' # string to identify the name of the model

models = get_model_list()
print(models)


'''
simulated conversation where the user gives an initial question
to one LLM and then allows two LLMs to converse in a loop
 '''
 
print("User: \nHi, how are you?")
input_string = 'Hi, how are you?'
response = call_and_respond(model_name, input_string)

for i in range(3):
    print("tinyllama: ")
    response = call_and_respond('tinyllama:latest', response)
    print("smollm: ")
    response = call_and_respond('smollm:latest', response)
    
