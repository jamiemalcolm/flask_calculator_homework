from app import app
from modules.calculator_tests import *

@app.route('/add/<number1>/<number2>')
def addition(number1, number2):
    return f"this equals {add(number1, number2)}"

@app.route('/subtract/<number1>/<number2>')
def subtraction(number1, number2):
    return f"this equals {subtract(number1, number2)}"
    
@app.route('/divide/<number1>/<number2>')
def division(number1, number2):
    return f"this equals {divide(number1, number2)}"

@app.route('/multiply/<number1>/<number2>')
def multiplication(number1, number2):
    return f"this equals {multiply(number1, number2)}"

@app.route('/square/<number1>')
def squaring(number1):
    return f"this equals {squared(number1)}"