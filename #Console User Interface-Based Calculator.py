#Console User Interface-Based Calculator

import os
from enum import Enum

class Operator(Enum):
    addition = 0
    subtraction = 1
    multiplication = 2
    equal = 3

def is_exit(var):
    if var == 'q':
        exit()
    else:
        return var

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
        return false

def error_detector(operator, operand1, operand2):
    if not operator_kind(operator):
        print("잘못된 연산자입니다.")
        return false
    if not isinstance(operand1, int) or not isinstance(operand2, int):
        print("잘못된 피연산자입니다.")
        return false
    return true

def calcuate(operand1, operator, operand2):
    if operator == Operator.addition:
        return operand1 + operand2
    elif operator == Operator.subtraction:
        return operand1 - operand2
    elif operator == Operator.multiplication:
        return operand1 * operand2

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    operand1 = operand2 = None
    
    clear_console()
    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
    print("종료하려면 'q'를 입력하세요.")

    while true:
        operand1 = is_exit(input("피연산자를 입력하세요: "))
        operator = is_exit(operator_kind(input("연산자를 입력하세요: ")))
        operand2 = is_exit(input("피연산자를 입력하세요: "))
        if not error_detector(operator, operand1, operand2):
            print("잘못된 값이 입력됐습니다. 처음부터 다시 입력하세요.")
            continue
        break

    tmp = calcuate(operand1, operator, operand2)
    
    while True:
        while true:
            operator = is_exit(operator_kind(input("연산자를 입력하세요: ")))
            if operator == Operator.equal:
                print(" " + tmp)    #등호 입력되고나면 tmp가 0이 되나? 아니면 계속 유지하나?
                continue
            operand2 = is_exit(input("피연산자를 입력하세요: "))
            if not error_detector(operator, tmp, operand2):
                print("잘못된 값이 입력됐습니다. 마지막 피연산자와 연산자를 입력하세요.")
                continue
            break
        tmp = calcuate(tmp, operator, operand2)

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
