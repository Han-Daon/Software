from enum import Enum

class Operator(Enum):
    none = 0
    addition = 1
    subtraction = 2
    multiplication = 3
    equal = 4
    egg = 5

def is_right_operand(operand):
    index = 0
    if operand[0] == '-':   #음수인 경우
        index = 1
    for i in range(index, len(operand)):
        if not 48 <= ord(operand[index]) <= 57:
            return False
        index = index + 1
    return operand

def is_right_operator(operator):
    if operator == '+':
        return Operator.addition
    elif operator == '-':
        return Operator.subtraction
    elif operator == '*' or operator == 'x' or operator == 'X':
        return Operator.multiplication
    elif operator == '=':
        return Operator.equal
    else:
        return False

def calculate(operand1, operator, operand2):
    if operator == Operator.addition:
        return int(operand1) + int(operand2)
    elif operator == Operator.subtraction:
        return int(operand1) - int(operand2)
    elif operator == Operator.multiplication:
        return int(operand1) * int(operand2)
    elif operator == Operator.none or opperand2 == None:
        return int(operand1)
