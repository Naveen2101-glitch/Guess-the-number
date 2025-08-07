import random

num = random.randint(1, 100)
guess = int(input("Enter the number: "))

while num != guess:
    if guess > num:
        print("Your number is too high")
    else:
        print("Your number is too low")
    guess = int(input("Enter the number again: "))

print("You Won!")
