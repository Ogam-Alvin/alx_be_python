def perform_operation(num1:float, num2: float, operation:str):#num1 and num2 are the variables to be used, and operation is the task to be performed
    if operation =='add':
        return num1+num2
    elif operation == 'subtract':
        return num1-num2
    elif operation == 'multiply':
        return num1*num2
    elif operation == 'divide':
        return num1/num2
    else:
        return 'Error:Invalid operation'
    