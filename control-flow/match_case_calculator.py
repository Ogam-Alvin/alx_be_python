#Prompt the user to enter two numbers
number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))
#Perform calculations using the match case
match operation:
    case '+':
        result = number1 + number2
    case '-':
        result = number1-number2
    case'*':
        result = number1*number2
    case '/':
        if number2==0:
            print('Cannot divide by zero')
        else:
            result = number1/number2
    case _:
        print('Invalid Operation. Select between "+", "-", "*", or "/"')

print(f'The result is {result}')