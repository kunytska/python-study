print('Hi! Please enter number')
def is_number(string):
    try:
        x = float(string)
        return True
    except:
        return False

result = 0
operation = ''
while True:
    command = input()
    if command == 'exit':
        break
    if command == '+' or command == '-' or command == '*' or command == '/':
        operation = command

    else:
        if is_number (command):
            number = float(command)
            if operation == '':
                result = number
            else:
                if operation == '+':
                    result = result + number
                elif operation == '-':
                    result = result - number
                elif operation == '*':
                    result = result * number
                elif operation == '/':
                    if number == 0:
                        print('Ти олень!')
                    else:
                        result = result / number
            operation = ''
            print(result)
        else:
            print('Expected operation or number')

