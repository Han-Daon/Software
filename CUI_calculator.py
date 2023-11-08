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
from enum import Enum #os 모듈과 Enum 클래스를 불러옵니다. os는 운영 체제와 상호 작용할 수 있게 해주며, Enum은 열거형(Enumerated Type)을 정의하는 데 사용됩니다.

#사용자가 'q'를 입력하면 프로그램을 종료하고, 그렇지 않으면 입력 값을 반환.
def is_exit(var): 
    if var == 'q':
        exit()
    else:
        return var

#계산기에서 사용할 연산자들을 열거형으로 정의
class Operator(Enum):
    none = 0
    addition = 1
    subtraction = 2
    multiplication = 3
    equal = 4

#오류 유형을 열거형으로 정의
class Error(Enum):
    none = 0
    operator = 1
    operand = 2

#입력받은 문자열 연산자를 해당하는 Operator 열거형으로 변환
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

#두 피연산자와 연산자를 받아, 해당 연산을 수행하고 결과를 반환
def calculate(operand1, operator, operand2):
    if operator == Operator.addition:
        return int(operand1) + int(operand2)
    elif operator == Operator.subtraction:
        return int(operand1) - int(operand2)
    elif operator == Operator.multiplication:
        return int(operand1) * int(operand2)
    elif operator == Operator.none:
        return int(operand1)

#연산자와 피연산자들을 검사하여 오류가 있으면 해당 오류 유형을 반환하고, 없으면 Error.none을 반환
def is_error(operator, operand1, operand2):
    if not operator:
      print("잘못된 연산자입니다.")
      return Error.operator
    if not is_right_operand(str(operand1)) or not is_right_operand(str(operand2)):
      print("잘못된 피연산자입니다.")
      return Error.operand
    return Error.none

#피연산자가 올바른지 검사합니다. 피연산자가 음수일 경우 '-'(음수)을 제외하고 검사
def is_right_operand(operand):
  index = 0
  if operand[0] == '-':   #음수인 경우
    index = 1
  for i in range(index, len(operand)):
    if not 48 <= ord(operand[index]) <= 57:
      return False
    index = index + 1
  return True

#콘솔 화면을 지워줍니다. 운영 체제가 유닉스 계열일 경우 'clear'를, 윈도우일 경우 'cls'를 사용
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

#계산기 프로그램의 메인 로직을 수행. 연산 결과를 저장하는 변수, 연산자를 저장하는 변수, 피연산자를 저장하는 변수를 선언하고, 사용자에게 연산자와 피연산자를 입력받아 계산을 수행
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
#크립트가 직접 실행될 때 main() 함수를 호출함. 이 코드로 인해 이 스크립트는 모듈로 불러와져 사용되는 경우에는 main() 함수가 호출되지 않음.
if __name__ == "__main__":
    main()
'''
