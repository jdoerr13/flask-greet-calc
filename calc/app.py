from flask import Flask, request
from operations import add, sub, mult, div 

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters. How to get the a & b parameters from the URL ?a=___&b=___"""
    a = int(request.args.get("a")) #The get() method of the request.args dictionary will return the value of the specified parameter, or None if the parameter is not present.
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Add a and b parameters. How to get the a & b parameters from the URL ?a=___&b=___"""
    a = int(request.args.get("a")) #The get() method of the request.args dictionary will return the value of the specified parameter, or None if the parameter is not present.
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Add a and b parameters. How to get the a & b parameters from the URL ?a=___&b=___"""
    a = int(request.args.get("a")) #The get() method of the request.args dictionary will return the value of the specified parameter, or None if the parameter is not present.
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Add a and b parameters. How to get the a & b parameters from the URL ?a=___&b=___"""
    a = int(request.args.get("a")) #The get() method of the request.args dictionary will return the value of the specified parameter, or None if the parameter is not present.
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

operation = {
    'add': add, #functions from operations.py
    'sub': sub,
    'mult': mult,
    'div': div
}
@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operation[oper](a, b)

    return str(result)