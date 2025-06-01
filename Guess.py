from random import randint

num = randint(1,100)
# print(num)
i = 0

while True:
    guess = int(input("Enter a number: "))
    i += 1
    
    if guess == num:
        print("Got it. Attempt: ", i)
        break
    elif guess > num:
        print("High. Attempt: ", i)
    else:
        print("Low. Attempt: ", i)
    
        