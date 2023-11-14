#Console User Interface-Based Calculator

import os

# Function to clear the console based on the operating system
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

# Function to print the calculator's user interface
def display_interface(expression):
    clear_console()
    print("간단한 CUI 계산기")
    print("사용 가능한 연산: +, -, *(곱셈)")
    print("종료하려면 'q'를 입력하세요.")
    print("=" * 20)
    print("현재 수식:", expression)
    print("=" * 20)

# Function to evaluate the expression and return the result
def calculate_expression(expression):
    try:
        return eval(expression), False
    except Exception as e:
        return e, True

# Function to print errors and instructions
def print_error_continue(msg):
    print(msg)
    input("아무 키나 누르면 계속하세요...")

# The main function that orchestrates the calculator operations
def main():
    expression = ""
    error_flag = False

    while True:
        display_interface(expression)
        user_input = input("연산자나 피연산자를 입력하세요: ")

        if user_input == 'q':
            break
        elif user_input in ['+', '-', '*']:
            expression += user_input
            error_flag = False
        elif user_input.isdigit():
            expression += user_input
            if '.' in expression:
                error_flag = True  # 실수가 입력된 경우 에러 플래그 설정
        elif user_input == '=':
            if error_flag:
                print_error_continue("ERROR! 잘못된 수식입니다.")
                expression = ""
                error_flag = False
            else:
                result, error_flag = calculate_expression(expression)
                if not error_flag:
                    print(f"= {result}")
                    input("아무 키나 누르면 계속하세요...")
                    expression = ""
                else:
                    print_error_continue(f"ERROR! {result}")
                    expression = ""
        else:
            expression += user_input
            error_flag = True

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
