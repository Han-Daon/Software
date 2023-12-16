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

# 피연산자가 올바른지 검사합니다. 피연산자가 음수일 경우 '-'(음수)을 제외하고 검사
def is_right_operand(operand):
    index = 0
    if operand[0] == '-':   #음수인 경우
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
    elif operator == '!': #add for factorial
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
    elif operator == Operator.factorial: #add for factorial
        if operand1 < 0: #add for additional error (for operand less than 0)
            print("[ERROR] Out Of Range")
            return -1
        fac_result = 1
        multiplier = operand1
        if operand1 == 0:
            return 1
        else:
            for i in range(operand1):
               fac_result = fac_result * multiplier
               multiplier = multiplier - 1
            return fac_result
    elif operator == Operator.none or operand2 == None:
        return int(operand1)
    else:
        return -2 #Error of Input, operator is not operator!

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
        if turn == Turn.Operand:     # 이전 루프에서 연산자 혹은 잘못된 피연산자를 입력받음
            user_input = input("피연산자를 입력하세요: ")
        else:                       # 이전 루프에서 피연산자 혹은 잘못된 연산자를 입력받음
            user_input = input("연산자를 입력하세요: ")
            
        # 이스터에그 체크 & 이스터에그 입력 즉시 바로 출력 및 종료
        if user_input in egg:
            print("[EVENT] " + egg[user_input])
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
            
            if user_input == '!':
               print("[ERROR] Input Error") #if two or more individual numbers are placed before
               result = calculate(operand, operator, user_input)
               exit()       
            
            turn = Turn.Operator # 다음 입력은 연산자
                  
        else:
            operator = is_right_operator(user_input)

            if operator == Operator.equal and operator != Operator.factorial:
                if error:
                    print("[SYSTEM] ERROR!")
                else:
                    print(result)
                exit()
            
            if operator == Operator.factorial: #add for factorial
                if error:
                    if user_input == '!':
                       result = calculate(operand, operator, 0)
                       print("[ERROR] Input Error") #if two or more individual numbers are placed before
                       exit() 
                    print("[SYSTEM] ERROR!")
                else:
                    result = calculate(result, operator, 0)
                    if result > 0:
                        print(result)
                exit()

            # 이전에 오류가 없었다면 입력 체크
            if not error:

                # 연산자 오류 체크
                if not operator:
                    error = True

            turn = Turn.Operand # 다음 입력은 피연산자

#==========================================================================================================
#Now, Let's make the Test case for project!

#1. Unit test for some functions and Class: Class Turn, Operator, calculate
class TestOperand(unittest.TestCase):
    def testOperand(self):
        self.assertEqual(is_right_operand('1'), '1')
        #fill in here!

class TestOperator(unittest.TestCase):
    def testOperator(self):
        self.assertEqual(is_right_operator("+"), Operator.addition)
        #fill in here!

class TestCalculate(unittest.TestCase):
    def testCalculate(self):
        self.assertEqual(calculate(1, Operator.multiplication, 3), 3)
        #fill in here!

#2. Test Case for TDD(factorial function)
class TestFactorial(unittest.TestCase):
    def testBasicFactorial(self):
        self.assertEqual(calculate(3, Operator.factorial, 0), 6)
        self.assertEqual(calculate(5, Operator.factorial, 0), 120)
        
    def testMinusFactorial(self):
        self.assertEqual(calculate(-3, Operator.factorial, 0), -1)
        self.assertEqual(calculate(-10, Operator.factorial, 0), -1)

    def testAdvanceFactorial(self):
        self.assertEqual(calculate(3, 5, Operator.factorial), -2)
        self.assertEqual(calculate(4, 9, Operator.factorial), -2)
        


#==========================================================================================================

if __name__ == "__main__":
    main()
    
    #테스트를 하려면 main() 대신 이 아래의 주석 부분을 해제하세요. :)
    #suite = unittest.TestSuite()
    
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOperand))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOperator))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculate))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFactorial))
    
    #unittest.TextTestRunner().run(suite)
