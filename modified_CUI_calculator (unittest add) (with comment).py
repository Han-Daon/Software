# Console User Interface-Based Calculator
import os
from enum import Enum
import msvcrt

#for making test case(Automatic testing)
import unittest


# 이스터에그
egg = {"100":"백점!", "10000":"만세!!!", "1015":"전북대 개교기념일입니다."}

# Operator라는 이름의 열거형(Enum) 클래스를 정의합니다.
# 각각의 연산자를 나타내는 상수를 정의합니다.
class Operator(Enum):
    none = 0
    addition = 1
    subtraction = 2
    multiplication = 3
    equal = 4
    egg = 5
    factorial = 6

# 피연산자가 올바른지 검사하는 함수입니다.
# 피연산자가 숫자인지를 확인합니다.
def is_right_operand(operand):
    index = 0
    # 피연산자가 음수일 경우 '-'(음수)을 제외하고 검사합니다.
    if operand[0] == '-':   
        index = 1
    # 피연산자의 각 문자가 숫자인지 확인합니다.
    for i in range(index, len(operand)):
        if not 48 <= ord(operand[index]) <= 57:
            return False
        index = index + 1
    return operand

# 입력받은 문자열 연산자를 해당하는 Operator 열거형으로 변환하는 함수입니다.
def is_right_operator(operator):
    if operator == '+':
        return Operator.addition
    elif operator == '-':
        return Operator.subtraction
    elif operator == '*' or operator == 'x' or operator == 'X':
        return Operator.multiplication
    elif operator == '!':
        return Operator.factorial
    elif operator == '=':
        return Operator.equal
    else:
        return False

# 두 피연산자와 연산자를 받아, 해당 연산을 수행하고 결과를 반환하는 함수를 정의합니다.
def calculate(operand1, operator, operand2):
    if operator == Operator.addition:  # 덧셈 연산
        return int(operand1) + int(operand2)
    elif operator == Operator.subtraction:  # 뺄셈 연산
        return int(operand1) - int(operand2)
    elif operator == Operator.multiplication:  # 곱셈 연산
        return int(operand1) * int(operand2)
    elif operator == Operator.factorial:  # 팩토리얼 연산
        if operand1 < 0:  # 팩토리얼은 음수에 대해서는 정의되지 않습니다.
            return -1
        elif operand1 == 0:  # 0의 팩토리얼은 1입니다.
            return 1
        else:  # 팩토리얼 계산
            fac_result = 1
            for i in range(operand1):
               fac_result = fac_result * (i+1)
            return fac_result
    elif operator == Operator.none or operand2 == None:  # 연산자가 없거나 피연산자가 없는 경우
        return int(operand1)
    else:  # 그 외의 경우
        return False

# 다음 연산의 유형을 열거형으로 정의합니다.
# 연산자와 피연산자를 구분하기 위해 사용합니다.
class Turn(Enum):
    Operator = 0
    Operand = 1

# 콘솔 화면을 지워주는 함수를 정의합니다.
# 운영 체제가 유닉스 계열일 경우 'clear'를, 윈도우일 경우 'cls'를 사용합니다.
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

# 메인 함수를 정의합니다.
def main():
    # 필요한 변수들을 초기화합니다.
    result = 0
    operator = Operator.addition
    error = False

    # 사용자에게 CUI 계산기에 대한 정보를 출력합니다.
    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
 
    # 이번에 어떤 종류의 입력을 받을지를 나타내는 변수입니다.
    turn = Turn.Operand 
    user_input = Operator.none

    while True:
        operand = None
        # 피연산자 입력받을 차례인 경우
        if turn == Turn.Operand:
            user_input = input("피연산자를 입력하세요: ")
        # 연산자 입력받을 차례인 경우
        else:
            user_input = input("연산자를 입력하세요: ")
            
        # 이스터에그 입력 즉시 출력 및 종료
        if user_input in egg:
            print("[EVENT] " + egg[user_input])
            exit()

        # 피연산자 입력받을 차례
        if turn == Turn.Operand:
            # 입력받은 피연산자가 올바른지 확인합니다.
            operand = is_right_operand(user_input)

            # 피연산자가 올바르지 않은 경우 오류 메시지를 출력하고 종료합니다.
            if not operand:
                error = True
                if user_input == "=":
                    print("[SYSTEM] ERROR!")
                    exit()
                elif user_input == "!":
                    print("[SYSTEM] Input ERROR!")
                    return "[SYSTEM] Input ERROR!"
            # 피연산자가 올바른 경우 계산을 수행합니다.
            else:
                result = calculate(result, operator, operand)    
            
            # 다음 입력은 연산자입니다.
            turn = Turn.Operator 

        # 연산자 입력받을 차례 
        else:
            # 입력받은 연산자가 올바른지 확인합니다.
            operator = is_right_operator(user_input)

            # 연산자가 올바르지 않은 경우 오류 메시지를 출력합니다.
            if not operator:
                error = True
            else:
                # '=' 연산자인 경우 계산 결과를 출력하고 종료합니다.
                if operator == Operator.equal:
                    if error:
                        print("[SYSTEM] ERROR!")
                    else:
                        print(result)
                    exit()
                # '!' 연산자인 경우 팩토리얼 계산을 수행하고 결과를 출력한 후 종료합니다.
                elif operator == Operator.factorial:
                    if error:
                        print("[ERROR] Input Error")
                    else:
                        result = calculate(result, operator, 0)
                        if result == -1:
                            print("[ERROR] Out Of Range")
                        else:
                            print("={}".format(result))
                    exit()
                    
            # 다음 입력은 피연산자입니다.
            turn = Turn.Operand 
#==========================================================================================================

#1. 유닛테스트
# 사용 메서드
# is_right_operand
# is_right_operator
# calculate
class TestOperand(unittest.TestCase):
    def testOperand(self):
        self.assertEqual(is_right_operand('1'), '1')
        #입력받은 피연산자를 판별하는 테스트케이스

    def testOperand2(self):
        self.assertEqual(is_right_operand('-1'), '-1')
        #피연산자에 음수 값 입력 시 판별하는 테스트케이스

    def testOperand3(self):
        self.assertEqual(is_right_operand('+1'), False)
        #피연산자에 유효하지 부호 입력 시 판별하는 테스트케이스
        
    def testSymbolOperand(self): #특수기호를 Symbol 적음
        self.assertEqual(is_right_operand('@'), False)
        #피연산자에 특수기호를 입력 시 판별하는 테스트케이스
    
class TestOperator(unittest.TestCase):
    def testOperator(self):
        self.assertEqual(is_right_operator("+"), Operator.addition)
        #입력받은 더하기 문자를 Operator 열거형으로 알맞게 변환하는지 판별하는 테스트케이스
    def testOperator2(self):

        self.assertEqual(is_right_operator("X"), Operator.multiplication)
        #입력받은 곱 문자의 여러 조건중 하나를 택하여 열거형으로 알맞게 변환하는지 판별하는 테스트케이스
    def testOperator3(self):

        self.assertEqual(is_right_operator("+"), Operator.multiplication)
        #입력받은 연산자가 알맞은 Operator 열거형으로 알맞게 변환하는지 판별하는 테스트케이스
        #fail

    def testOperator4(self):
        self.assertEqual(is_right_operator("/"), False)
        #Operator에 존재하지 않는 연산자나 특수기호 사용을 판별하는 테스트케이스

class TestCalculate(unittest.TestCase):
    def testCalculate(self):
        self.assertEqual(calculate(1, Operator.multiplication, 3), 3)
        #기본 기능을 수행하는지 확인하는 테스트케이스

    def testCalculate2(self):
        self.assertEqual(calculate(-1, Operator.multiplication, 3), -3)
        #음수 값의 피연산자의 연산을 확인하는 테스트케이스

    def testCalculate3(self):
        self.assertEqual(calculate(Operator.multiplication, 1, 3), False)
        #연산자와 피연산자 올바른 입력순서를 판단하는 테스트케이스

#2. TDD 테스트케이스
class TestFactorial(unittest.TestCase):
    def testBasicFactorial(self):
        self.assertEqual(calculate(3, Operator.factorial, 0), 6)
        self.assertEqual(calculate(5, Operator.factorial, 0), 120)
        #팩토리얼이 기본적으로 실행되는지 확인하는 테스트케이스

    def testMinusErrorFactorial(self):
        self.assertEqual(calculate(-3, Operator.factorial, 0), -1)
        self.assertEqual(calculate(-10, Operator.factorial, 0), -1)
        #음수 팩토리얼 입력시 오류 출력을 확인하는 테스트케이스 
        #오류시 해당 메서드는 -1로 출력

    def testAdvanceFactorial(self):
        self.assertEqual(calculate(3, 5, Operator.factorial), False)
        self.assertEqual(calculate(Operator.factorial, 5, 6), False)
        #기본적인 연산자와 피연산자의 조합순서에 팩토리얼이 잘 작동하는지 확인하는 테스트케이스


#==========================================================================================================

if __name__ == "__main__":
    # main()
    
    #테스트를 하려면 main() 대신 이 아래의 주석 부분을 해제
    suite = unittest.TestSuite()
    
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOperand))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOperator))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculate))

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFactorial))

    unittest.TextTestRunner().run(suite)
