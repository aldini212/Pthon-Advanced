def greet_person (name, greeting ="Hello"):
    message = f"{greeting},{name}"
    return(message)

default_greeting = greet_person("Alice")
print(default_greeting)

custom_greeting = greet_person("hi,bob")
print(custom_greeting)