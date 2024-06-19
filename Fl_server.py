from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def test():
    return 'welcome'

@app.route('/data/')
def dataset():
    return 'This is a dataset'

@app.route('/class/1/')
def class_1():
    return 'Class No.1'



app.run(port=5001, debug=True)