# Put your app in here. 
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def on_add():
    #^^^why cant this function name be the same as an imported function name for ex. add() instead of on_add()?
    a = int(request.args["a"]) 
    b = int(request.args.get("b"))
    #^^^why does the solution use parenthesis instead of square brackets?
    print(a, b)
    print(type(a), type(b))
    return str(add(a, b))
    #^^^why does this fail when its not converted to a str object?

@app.route('/sub')
def on_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route('/mult')
def on_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route('/div')
def on_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
    }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
