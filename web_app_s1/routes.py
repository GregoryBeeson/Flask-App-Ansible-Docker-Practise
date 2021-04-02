from flask import Flask, render_template
from __init__ import app
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')