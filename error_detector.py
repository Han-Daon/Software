from enum import Enum

class Error(Enum):
    none = 0
    operator = 1
    operand = 2

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
