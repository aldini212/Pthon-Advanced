from watchdog.observers.fsevents2 import message

gretting ="Hello"

def greet(name):

"""Delcaring a "Message" as a global variable"""

global  message
message = f"{greeting}, {name}"
print(message)

greet("Bob")
print(message)

 message = f"{greeting} , student"
print(message)
