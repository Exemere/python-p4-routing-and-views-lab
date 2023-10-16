#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return'<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:name>')
def print_string(name):
    print (name)
    return f'{name}'
    
@app.route('/count/<int:num>')
def count(num):
    return f"Counting from 1 to {num}"
pass

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    return f"{num1} {operation} {num2}"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
