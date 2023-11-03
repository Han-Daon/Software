#Console User Interface-Based Calculator

import os
from calculator import *
from error_detector import *

def is_exit(var):
    if var == 'q':
        exit()
    else:
        return var

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    result = 0
    operand = None
    operator = Operator.addition
    
    clear_console()
    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
    print("종료하려면 'q'를 입력하세요.")

    user_input = Operator.none  #피연산자 먼저 입력받게 함

    while True:
      if(type(user_input) == Operator):   #이전 루프에서 연산자를 입력받음 혹은 잘못된 피연산자를 입력받음
        user_input = is_exit(input("피연산자를 입력하세요: "))
        operand = user_input
      else:                               #이전 루프에서 피연산자를 입력받음 혹은 잘못된 연산자를 입력받음
        user_input = operator_kind(is_exit(input("연산자를 입력하세요: ")))
        operator = user_input
        if (operator == Operator.equal):
          print(str(result))
          user_input = operand   #등호인 경우 다음 루프에서 연산자를 입력받음
          continue
      
      error = is_error(operator, result, operand)

      if(error == Error.operand):
        user_input = operator   #다음 루프에서 피연산자를 입력받음
      elif(error == Error.operator):
        user_input = operand    #다음 루프에서 연산자를 입력받음
      elif(type(user_input) != Operator):
        result = calculate(result, operator, operand)

if __name__ == "__main__":
    main()

'''
합본
#Console User Interface-Based Calculator

import os
from enum import Enum

def is_exit(var):
    if var == 'q':
        exit()
    else:
        return var

class Operator(Enum):
    none = 0
    addition = 1
    subtraction = 2
    multiplication = 3
    equal = 4

class Error(Enum):
    none = 0
    operator = 1
    operand = 2

def operator_kind(operator):
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
    elif operator == Operator.none:
        return int(operand1)

def is_error(operator, operand1, operand2):
    if not operator:
      print("잘못된 연산자입니다.")
      return Error.operator
    if not is_right_operand(str(operand1)) or not is_right_operand(str(operand2)):
      print("잘못된 피연산자입니다.")
      return Error.operand
    return Error.none

def is_right_operand(operand):
  index = 0
  if operand[0] == '-':   #음수인 경우
    index = 1
  for i in range(index, len(operand)):
    if not 48 <= ord(operand[index]) <= 57:
      return False
    index = index + 1
  return True

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    result = 0
    operand = None
    operator = Operator.addition
    
    clear_console()
    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
    print("종료하려면 'q'를 입력하세요.")

    user_input = Operator.none  #피연산자 먼저 입력받게 함

    while True:
      print("result = " + str(result))

      if(type(user_input) == Operator):   #이전 루프에서 연산자를 입력받음 혹은 잘못된 피연산자를 입력받음
        user_input = is_exit(input("피연산자를 입력하세요: "))
        operand = user_input
      else:                               #이전 루프에서 피연산자를 입력받음 혹은 잘못된 연산자를 입력받음
        user_input = operator_kind(is_exit(input("연산자를 입력하세요: ")))
        operator = user_input
        if (operator == Operator.equal):
          print(str(result))
          user_input = operand   #등호인 경우 다음 루프에서 연산자를 입력받음
          continue
      
      error = is_error(operator, result, operand)

      if(error == Error.operand):
        user_input = operator   #다음 루프에서 피연산자를 입력받음
      elif(error == Error.operator):
        user_input = operand    #다음 루프에서 연산자를 입력받음
      elif(type(user_input) != Operator):
        result = calculate(result, operator, operand)

if __name__ == "__main__":
    main()
'''
