#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:user_string>')
def print_string(user_string):
    print(user_string)
    return f"{user_string}"

@app.route('/count/<int:parameter>')
def count(parameter):
    count = []
    for i in range(parameter):
        count.append(f"{i}\n")
    count_string = "".join(count)  
    return count_string

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    num_1 = int(num1)
    num_2 = int(num2)
    
    if operation == "+" :
        return f"{num_1 + num_2}"
    elif operation == "-":
        return f"{num_1 - num_2}"
    elif operation == "*":
        return f"{num_1* num_2 }"
    elif operation == 'div':
        return f"{num_1 / num_2}"
    elif operation == '%':
        return f"{num_1 % num_2}"




if __name__ == '__main__':
    app.run(port=5555, debug=True)
