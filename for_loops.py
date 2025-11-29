names = ["Alice","Donald","david","charlie"]
for name in names:
    print(name)

    sentence = "Hello, World!"

    for ch in sentence:
        if ch.isalpha():
            print(ch)

    for number in range (1,5000):
        print(number)

numbers=[12,45,6,7,94]

max = numbers[0]

    for num in numbers:
        if num > max:
            max = num

print("maksimumi eshte:",max)
