# Console User Interface-Based Calculator
import os
from enum import Enum
import msvcrt

#for making test case(Automatic testing)
import unittest


# 이스터에그
egg = {"100":"백점!", "10000":"만세!!!", "1015":"전북대 개교기념일입니다."}

# 계산기에서 사용할 연산자들을 열거형으로 정의
class Operator(Enum):
    none = 0
    addition = 1
    subtraction = 2
    multiplication = 3
    equal = 4
    egg = 5
    factorial = 6

# 피연산자가 올바른지 검사
def is_right_operand(operand):
    index = 0
    if operand[0] == '-':   #음수일 경우 '-'(음수)을 제외하고 검사
        index = 1
    for i in range(index, len(operand)):
        if not 48 <= ord(operand[index]) <= 57:
            return False
        index = index + 1
    return operand

# 입력받은 문자열 연산자를 해당하는 Operator 열거형으로 변환
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

# 두 피연산자와 연산자를 받아, 해당 연산을 수행하고 결과를 반환
def calculate(operand1, operator, operand2):
    if operator == Operator.addition:
        return int(operand1) + int(operand2)
    elif operator == Operator.subtraction:
        return int(operand1) - int(operand2)
    elif operator == Operator.multiplication:
        return int(operand1) * int(operand2)
    elif operator == Operator.factorial:
        if operand1 < 0:
            return -1
        elif operand1 == 0:
            return 1
        else:
            fac_result = 1
            for i in range(operand1):
               fac_result = fac_result * (i+1)
            return fac_result
    elif operator == Operator.none or operand2 == None:
        return int(operand1)
    else:
        return False

# 다음 연산의 유형을 열거형으로 정의
class Turn(Enum):
    Operator = 0
    Operand = 1

# 콘솔 화면을 지워줍니다. 운영 체제가 유닉스 계열일 경우 'clear'를, 윈도우일 경우 'cls'를 사용
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    # 변수 초기화
    result = 0
    operator = Operator.addition
    error = False

    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
 
    turn = Turn.Operand # 이번에 어떤 종류의 입력을 받을지
    user_input = Operator.none

    while True:
        operand = None
        if turn == Turn.Operand:
            user_input = input("피연산자를 입력하세요: ")
        else:
            user_input = input("연산자를 입력하세요: ")
            
        # 이스터에그 입력 즉시 출력 및 종료
        if user_input in egg:
            print("[EVENT] " + egg[user_input])
            exit()

        # 피연산자 입력받을 차례 ========================
        if turn == Turn.Operand:

            operand = is_right_operand(user_input)
                
            # 피연산자 오류 체크
            if not operand:
                error = True
                if user_input == "=":
                    print("[SYSTEM] ERROR!")
                    exit()
                elif user_input == "!":
                    print("[SYSTEM] Input ERROR!")
                    return "[SYSTEM] Input ERROR!"
            # 정상 입력이면 계산
            else:
                result = calculate(result, operator, operand)    
            
            turn = Turn.Operator # 다음 입력은 연산자

                
        # 연산자 입력받을 차례 =========================
        else:
            operator = is_right_operator(user_input)

            # 연산자 오류 체크
            if not operator:
                error = True
            else:
                if operator == Operator.equal:
                    if error:
                        print("[SYSTEM] ERROR!")
                    else:
                        print(result)
                    exit()
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
                    
            turn = Turn.Operand # 다음 입력은 피연산자

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
