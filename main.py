# name = "Vinay"

# print("Hello World")

# variable Type

# print(type(name))

# python data types

# a = 1
# b = 2.5
# c = 1 + 2j
# d = "Hello"
# # we have to use uppercase for True, False and None
# e = True
# no = None
# print(type(no))

# Python is case sensitive

# a = 5
# b = 10
# diff = a - b
# print(diff)

# Age Checker

# age = 18
#
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# Traffic Light Code

# light = input("Enter the light color: ")
#
# if(light == "red" or light == "Red"):
#     print("Stop")
# elif(light == "yellow" or light == "Yellow"):
#     print("Ready")
# else:
#     print("Go")



# Terneray Operator

# food = input("Enter the food name: ")
# print("Sweet" if food =="Cake" or food == "Jalebi" else "not sweet")

# Clever way to use Terneray Operator

# age = int(input("Enter the age: "))
# False value, True Value
# vote = ("No", "Yes")[age > 18]
# print(vote)



# Practice

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter First Number: "))
# sum = num1 + num2
# print("Sum of two numbers is: ", sum)


# side = int(input("Enter the side of square: "))
# area = side * side
# print("Area of square is: ", area)

# String Methods

# str = "Vinaypartap Singh"
# print(str[-6:-1])

# methods
# print(str.endswith("h"))
# print(str.capitalize())
# print(str.count("a"))
# print(str.find("a"))
# print(str.index("a"))
# print(str.replace("Vinaypartap Singh", "Manpreet Kaur"))

# username = input("Enter the username: ")
#
# print("Welcome", username)
# print(len(username))

# Arrays are lists in python

# arr = [1, 2, 3, 4, 5]

# print(type(arr))
# print(arr[0])
# print(arr[1:3])
# list methods

# arr.append(6)
# arr.sort()
# arr.reverse()
# arr.remove(3)
# arr.pop(3)
# print(arr)


# Dictionary in Python

info = {
    "name": "Vinay",
    "age": 21,
    "city": "Ludhiana",
    "skills": {"python", "java", "c++"},
    "subjects": {
        "1": "Maths",
        "2": "Science",
        "3": "English"
    }
}
# TO Access the dictionary elements
# print(info["name"])
# info["name"] = "Manpreet"
# print(info["skills"])
# print(info["name"])
# print(info["subjects"]["1"])
# print(list(info.keys()))
#print(list(info.values()))


# Recursion


def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)


# Factorial

def fact (n) :
    if(n== 0 or n==1):
        return 1
    return n * fact(n-1)


print(fact(5))