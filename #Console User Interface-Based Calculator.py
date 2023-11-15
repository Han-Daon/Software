#Console User Interface-Based Calculator
import os
from enum import Enum
import msvcrt

#계산기에서 사용할 연산자들을 열거형으로 정의
class Operator(Enum):
    none = 0
    addition = 1
    subtraction = 2
    multiplication = 3
    equal = 4
    egg = 5

#피연산자가 올바른지 검사합니다. 피연산자가 음수일 경우 '-'(음수)을 제외하고 검사
def is_right_operand(operand):
    index = 0
    if operand[0] == '-':   #음수인 경우
        index = 1
    for i in range(index, len(operand)):
        if not 48 <= ord(operand[index]) <= 57:
            return False
        index = index + 1
    return operand

#입력받은 문자열 연산자를 해당하는 Operator 열거형으로 변환
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

#두 피연산자와 연산자를 받아, 해당 연산을 수행하고 결과를 반환
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

#다음 연산의 유형을 열거형으로 정의
class Turn(Enum):
    Operator = 0
    Operand = 1

#사용자가 'q'를 입력하면 프로그램을 종료하고, 그렇지 않으면 입력 값을 반환.
def is_exit(var):
    if var == 'q':
        exit()
    else:
        return var

#콘솔 화면을 지워줍니다. 운영 체제가 유닉스 계열일 경우 'clear'를, 윈도우일 경우 'cls'를 사용
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    #변수 초기화
    result = 0
    operator = Operator.addition
    error = False

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

        # 이스터에그 체크 & 이스터에그 입력 즉시 바로 출력 및 종료
        if user_input in egg:
            print(egg[user_input])
            exit()

        # 피연산자 입력받을 차례
        if turn == Turn.Operand:

            # 이전에 오류가 없었다면 입력 체크
            if not error:
                operand = is_right_operand(user_input)
                
                # 피연산자 오류 체크
                if not operand:
                    error = True
                # 정상 입력이면 계산
                else:
                    result = calculate(result, operator, operand)
                    
            turn = Turn.Operator #다음 입력은 연산자
                  
        else:
            operator = is_right_operator(user_input)

            if operator == Operator.equal:
                if error:
                    print("ERROR!")
                else:
                    print(result)
                exit()

            # 이전에 오류가 없었다면 입력 체크
            if not error:

                # 연산자 오류 체크
                if not operator:
                    error = True

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
