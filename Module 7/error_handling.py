from logging import exception

try:
        result = 10/0
except ZeroDivisionError:
    print("OOPS! tried to divide ny zero")

#execpt osht edhe nese ki ndonje error kjo ta lejon apet me barun qka kedasht veq me ni paralajmrin

fruits = {
    "apple": 5,
    "banana":7,
    "kiwi":3
}

try:
  print(fruits["orange"])

except KeyError:
    print("OHNO THE KEY DOSENT EXIST")

text = "this is not a number"
try:
    text_to_int = int(text)
except Exception as e:
    print("An error occurred while parsing data:" , e)


 #nese nuk e din qfar errori eshte mundesh me provu me exception as e

try:
    result = 10/0.5

except ZeroDivisionError:
    print("Division by zero error occured")
else:
    print("Division successful. Result:",result)

#finally block

try:
    result=10/0
except ZeroDivisionError:
    print("Cannot devide by zero")

finally:
    print("finally has been executed")

#Exercise
def divide_numbers(a,b):
    try:
        result = a / b
        print("result of division",result)
    except ZeroDivisionError:
        print("cannot devide by zero")
    except TypeError:
        print("Invalid type,")
    except Exception as e:
        print(f"Unxecpect error:{e}")

divide_numbers(10,2)
divide_numbers(10,0)
divide_numbers(10,"2")


