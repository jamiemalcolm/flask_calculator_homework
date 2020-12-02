from app import app
from modules.calculator_tests import *

@app.route('/add/<number1>/<number2>')
def addition(number1, number2):
    return f"this equals {add(number1, number2)}"
    
