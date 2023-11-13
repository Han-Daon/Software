#Console User Interface-Based Calculator

import os
from calculator import *
from error_detector import *

egg = {"1":"하나!", "2":"둘!!"}

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
