#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 15:50:01 2025

@author: elucidatspare
"""

# web server using flask
from flask import Flask, render_template, request, jsonify
from markupsafe import escape
import Ollama_ex

app = Flask(__name__)

#get models from Ollama for drop-down
model_list = Ollama_ex.get_model_list() 


@app.route('/')
def index(model_list=model_list, methods=['POST', 'GET']):
    if request.method == 'POST':
        text = request.form['input text']
        return text
    return render_template('index2.html', models=model_list, text="Blank")

@app.route('/button_func')
def button_func():
    output = Ollama_ex.call_and_respond("tinyllama:latest", "hello")
    return jsonify({"text": output})

if __name__ == "__main__":
    app.run(debug=True)