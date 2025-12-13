from Module1.variables import result


def greet():
    print ("pau ba mir ska qare")

greet()


def greet_person(name):
    print("Hello,",name)

greet_person("Hamburg")


'''
def add (x,y):
 z=x+y
 return z
 
 add(3,7)
'''


def add(x, y):
    z = x + y
    return  z



result = add(3,7)

print("here are the results =",result)

