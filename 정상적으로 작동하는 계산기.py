#Console User Interface-Based Calculator

import os

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    expression = ""
    error_flag = False  # 에러 플래그 추가

    while True:
        clear_console()
        print("간단한 CUI 계산기")
        print("사용 가능한 연산: +, -, *(곱셈)")
        print("종료하려면 'q'를 입력하세요.")
        print("=" * 20)
        print("현재 수식:", expression)
        print("=" * 20)

        user_input = input("연산자나 피연산자를 입력하세요: ")

        if user_input == 'q':
            break
        elif user_input in ['+', '-', '*']:
            expression += user_input
            error_flag = False  # 연산자 입력 시 에러 플래그 초기화
        elif user_input == '=':
            if error_flag == True:
                print("ERROR!")
                input("아무 키나 누르면 계속하세요...")
                expression = ""
            else:
                try:
                    result = eval(expression)
                    print(f"= {result}")
                    input("아무 키나 누르면 계속하세요...")
                    expression = ""
                except:
                    print("ERROR!")
                    input("아무 키나 누르면 계속하세요...")
                    expression = ""
        elif user_input.isdigit():
            expression += user_input
            if '.' in expression:
                error_flag = True  # 실수가 입력된 경우 에러 플래그 설정
            if expression == "7503":
                print("=> Software Interaction Lab.")
                input("아무 키나 누르면 계속하세요...")
                expression = ""
        else:
            error_flag = True  # '/' 입력 시 에러 플래그 설정
            expression += user_input

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
