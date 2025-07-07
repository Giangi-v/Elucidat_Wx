#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 15:50:01 2025

@author: elucidatspare
"""

# web server using flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'