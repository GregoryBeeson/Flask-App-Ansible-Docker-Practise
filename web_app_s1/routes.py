from flask import Flask, render_template
import requests
from __init__ import app
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
    test = requests.get('http://logic_s4:5004/logic')
    print("hello")
    print(test.text)
    test = test.text
    return render_template('test.html', test = test)