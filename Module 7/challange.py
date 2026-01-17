def calculate (number1, number2, operator):
    if operator == '+':
        return  number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        raise ValueError('Invalid operation')

try:
 num1 = float(input("Enter the first number:"))
 num2 = float(input("Enter the first two:"))
 operator = input("Enter an operator(+,-,*,/):")
 result = calculate (num1,num2,operator)
 print(f"Ma guy here is the result of {num1} {operator} {num2} is {result}")
except ValueError as e:
    print(f"invalid input: {e}")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as e:
    print(f"Unexecpted error occurred: {e}")
finally:
    print("End of the program")
