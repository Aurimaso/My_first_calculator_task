def calculator(num1, num2, todo):
    if (type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
        if todo == '+':
            return num1 + num2
        elif todo == '-':
            return num1 - num2
        elif todo == '*':
             return num1 * num2
        elif todo == '/':
            if num2 == 0:
                return 'Division by zero not possible'
            else:
                 return num1 / num2
        else:
            return 'This calculator does not understand this action.. :('
    else:
        return 'You can use only numbers for this calculator.'




