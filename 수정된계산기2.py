#Console User Interface-Based Calculator

import os
from enum import Enum
import msvcrt

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
    elif operator == Operator.none or operand2 == None:
        return int(operand1)

egg = {"20220222":"야 너네 자랑하고 싶은 거 있으면 얼마든지 해. 난 괜찮아 왜냐면 부럽지가 않어 한 개도 부럽지가 않어"}

class Turn(Enum):
    Operator = 0
    Operand = 1

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

    turn = Turn.Operand #이번에 어떤 종류의 입력을 받을지
    user_input = Operator.none
    
    while True:
        operand = None
        if turn == Turn.Operand:     #이전 루프에서 연산자 혹은 잘못된 피연산자를 입력받음
            user_input = is_exit(input("피연산자를 입력하세요: "))
        else:                       #이전 루프에서 피연산자 혹은 잘못된 연산자를 입력받음
            user_input = is_exit(input("연산자를 입력하세요: "))

        #이스터에그 체크
        if user_input in egg:
            print(egg[user_input])
            continue

        #피연산자 에러 체크
        if turn == Turn.Operand:
            operand = is_right_operand(user_input)

            if not operand:
                print("잘못된 피연산자입니다.")
                continue
            
            turn = Turn.Operator #다음 입력은 연산자

            result = calculate(result, operator, operand)
            
        #연산자 에러 체크        
        else:
            operator = is_right_operator(user_input)

            if not operator:
                print("잘못된 연산자입니다.")
                continue
            
            if operator == Operator.equal:
                print(result)
                turn = Turn.Operator
                continue
            
            turn = Turn.Operand #다음 입력은 피연산자

if __name__ == "__main__":
    main()

# 테스트 케이스 1
# 15
# -
# 3
# -
# 10
# = 2

# 테스트 케이스 2
# 3
# *
# 1
# *
# 5
# = 15

# 테스트 케이스 3
# 3
# *
# 1
# /
# 5
# = ERROR!

# 테스트 케이스 4
# 3
# /
# 5
# = ERROR!

# 테스트 케이스 5
# 5.5
# *
# 2
# = ERROR!
