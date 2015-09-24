"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
while True:
    user_input = raw_input()
    user_input = user_input.split(" ")

    if user_input[0] == "+":
        print add(user_input[1], user_input[2])

    elif user_input[0] == "-":
        print substract(user_input[1], user_input[2])

    elif user_input[0] == "*":
        print multiply(user_input[1], user_input[2])

    elif user_input[0] == "/":
        print divide(user_input[1], user_input[2])

    elif user_input[0] == "square":
        print square(user_input[1])

    elif user_input[0] == "cube":
        print cube(user_input[1])

    elif user_input[0] == "power":
        print power(user_input[1], user_input[2])

    elif user_input[0] == "mod":
        print mod(user_input[1], user_input[2])
    
    elif user_input[0] == "q":
        break

    else: 
        print "enter an operator first"
