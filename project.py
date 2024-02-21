import random
import string

passlength = 12

charValues = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(passlength):
    password += random.choice(charValues)


print("Your Random Password is: " + password)