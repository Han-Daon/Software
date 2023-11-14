#Console User Interface-Based Calculator

import os
import keyboard
import time
from error_detector import *
from calculator import *

egg = {"100":"a+ 주세요", "200":"hello"}


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

current_input = ""
segment = 0

def on_key_event(e):
    global current_input, segment

    if e.event_type == keyboard.KEY_DOWN:
        current_input += e.name

        # 특정 입력 시 자동으로 출력
        if current_input == "7503":
            time.sleep(0.1)
            current_input = ""
            print(" => 123")
            segment = 1

def main():
    global segment
    result = 0
    operand = None
    operator = Operator.addition
    
    clear_console()
    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
    print("종료하려면 'q'를 입력하세요.")

    turn = Turn.Operand
    user_input = Operator.none
    
    while True:
        keyboard.hook(on_key_event)
        
        # 입력 받기
        if turn == Turn.Operand:
            user_input = is_exit(input("피연산자를 입력하세요: "))
        else:
            user_input = is_exit(input("연산자를 입력하세요: "))
        
        # 이스터에그 체크
        if user_input in egg:
            print(egg[user_input])
            continue

        # 피연산자 에러 체크
        if turn == Turn.Operand:
            operand = is_right_operand(user_input)

            if not operand:
                print("잘못된 피연산자입니다.")
                continue
            
            turn = Turn.Operator

            result = calculate(result, operator, operand)
            
        # 연산자 에러 체크        
        else:
            operator = is_right_operator(user_input)

            if not operator:
                print("잘못된 연산자입니다.")
                continue
            
            if operator == Operator.equal:
                print(result)
                turn = Turn.Operator
                continue
            
            turn = Turn.Operand

        # segment 값에 따라 루프 진행 방식 변경
        if segment == 1:
            segment = 0
            continue

if __name__ == "__main__":
    print("확인1")
    main()
    print("확인2")
