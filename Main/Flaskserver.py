#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 15:50:01 2025

@author: elucidatspare
"""

# web server using flask
from flask import Flask, render_template, request, jsonify, Response 
from markupsafe import escape
import json
import asyncio
import Ollama_ex
from collections import deque

LLM_selection = "tinyllama:latest"  # Default model selection

# LLM memory management
# Stack to store last 5 user inputs
user_input_stack = deque(maxlen=5)
LLM_output_stack = deque(maxlen=5)

def LLM_memory(user_input_text, LLM_output_text):
    # Handle user input history
    # Store the input in the stack
    user_input_stack.append(str(user_input_text))
    # Create a message history string
    message_history = ''
    count = 0
    for entry in user_input_stack:
        if count == 0:
            message_history = message_history + "Current input: " + entry + "\n"
        else:
            message_history = message_history + "Previous input: " + entry + "\n"
        count += 1

    # Handle LLM output history
    LLM_output_stack.append(str(LLM_output_text))
    # Create a LLM history string
    LLM_history = ''
    count = 0
    for entry in LLM_output_stack:
        if count == 0:
            LLM_history = LLM_history + "Most recent output: " + entry + "\n"
        else:
            LLM_history = LLM_history + "Previous output: " + entry + "\n"
        count += 1

    history = ("User input history:/n" + message_history + "/nLLM output history:/n" + LLM_history)
    return history 


app = Flask(__name__)

#get models from Ollama for drop-down
model_list = Ollama_ex.get_model_list() 

#load page
@app.route('/')
async def index(model_list=model_list):
    return render_template('index2.html', models=model_list, text="(Test output will appear here)", user_input_text=None)

#function acivated by test button
@app.route('/button_func')
async def button_func():
    output = Ollama_ex.call_and_respond("tinyllama:latest", "hello")
    return jsonify({"text": output})

#function to handle submission form
@app.route('/submit', methods=['POST'])
def submit_text():
    if request.method == 'POST':
        # Access the submitted text using the 'name' attribute from the HTML input field
        user_input_text = request.form.get('user_input', '')  # Get user input text
        previous_output_text = request.form.get('previous_output', '')  # Get previous output if available
        previous_output_text = previous_output_text[11:] if previous_output_text.startswith("LLM reply: ") else previous_output_text
        LLM_selection = request.form.get('LLM_selection', 'tinyllama:latest')  # Get selected model, default to 'tinyllama:latest'

        print(f"User input: {user_input_text}")
        print(f"Previous output: {previous_output_text}")
        print(f"\nSelected model: {LLM_selection}")

        if not user_input_text:
            return "No user input provided", 400

        
        # Function to generate a stream of responses from Ollama
        def generate_ollama_stream(MODEL_NAME, user_input_text, previous_output_text):
            LLM_input = LLM_memory(user_input_text, previous_output_text)
            messages = [{'role': 'user', 'content': LLM_input}]
            response_generator = Ollama_ex.chat(model=MODEL_NAME, messages=messages, stream=True)
            for chunk in response_generator:
                if chunk.get('message', {}).get('content'):
                    response_chunk = chunk['message']['content']
                    yield f"data: {json.dumps({'chunk': response_chunk})}\n\n"
            # Signal the end of the stream (optional, but good practice for SSE clients)
            yield "data: {}\n\n"

        # Return a Flask Response object with the generator and appropriate mimetype for SSE
        return Response(generate_ollama_stream(LLM_selection, user_input_text, previous_output_text), mimetype='text/event-stream')

    # If for some reason a GET request hits this route, redirect or show an error
    return "Method Not Allowed", 405


if __name__ == "__main__":

    app.run(debug=True)
