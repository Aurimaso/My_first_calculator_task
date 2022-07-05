def calculator(num1, num2, todo):
    try:
        if todo == '+':
            return num1 + num2
        elif todo == '-':
            return num1 - num2
        elif todo == '*':
             return num1 * num2
        elif todo == '/':
            if num2 == 0:
                return 'Division by zero not possible'           
            return num1 / num2    
        return 'This calculator does not understand this action.. :('
    # issiaikinti kas cia su tais exception
    except Exception as e:
        return 'You can use only numbers for this calculator.'

def calc_3nums(num1, num2, num3, todo1, todo2):
    if todo2 == '*' or '/':
        return calculator(num1, calculator(num2, num3, todo2), todo1)
    return calculator(calculator(num1, num2, todo1), num3, todo2)
        
# print(calc_3nums(2, 2, 2, '+', '*'))

def calculator_chooser(*args):
    count = 0
    for _ in args:
        count += 1
    if count == 3:
        return calculator(*args)
    elif count == 5:
        return calc_3nums(*args)
    return 'There was mistake, try again'
    

print(calculator_chooser(-2, -2, 4, '-','/'))

def calc_eval(x):
    try:
        return eval(x)
    except ZeroDivisionError:
        return 'No devision from zero'
    except SyntaxError:
        return 'Please try again :('
    


        
