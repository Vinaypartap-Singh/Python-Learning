import random
target = random.randint(1, 100)

while True:
    guess = int(input("Enter the number:"))
    if guess == target:
        print("Congratulations! You have guessed the number")
        break
    elif guess < target:
        print("Your guess is less than the target")
    else:
        print("Your guess is greater than the target")


print("<== End ==>")