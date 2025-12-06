

names = ["Alice","Donald","david","charlie"]
for name in names:
    print(name)

    sentence = "Hello, World!"

    for ch in sentence:
        if ch.isalpha():
            print(ch)

    for number in range (1,5):
        print(number)

numbers=[12,94.1,6,7,94.12]

max = numbers[0]

for num in numbers:
        if num > max:
            max = num

print("maksimumi eshte:",max)

count = 1

while count<= 5:
    print("rritje e vleres per nje: ",count)
    count+=1

numbers = [1,2,3,4,5,6,7,8,9,10,11]
target=9

for number in numbers:
    print(number)
    if number == target:
      print("Target Found")
      break

scores=[50,65,92,72,92,89,51,12]
total=0
count=0

for score in scores:
    if score <50:
        continue
    total+=score
    count+=1

mesatarja= total/count

print("opa kqyre mesataren", mesatarja)

while True:
    user_input=input("Jepe nje numer pozitiv:")
    if user_input.isnumeric():
        number= int(user_input)
        if number > 0:
            break
    print("Invalid. Try again")
print("You entered a positive number")

while True:
    user_input=input("Jepe nje numer qift:")
    if user_input.isnumeric():
        number= int(user_input)
        if number%2==0:
            break
    print("Invalid.  number tek")
print("You entered a numer qift")



