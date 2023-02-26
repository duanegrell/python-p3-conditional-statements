#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == "admin" and password == "12345":
        print("Access granted")
        return("Access granted")
    else: 
        print("Access denied")
        return("Access denied")

admin_login("sudo", "12345")

def hows_the_weather(temperature):
    if temperature < 40:
        print("It's brisk out there!")
        return "It's brisk out there!"
    elif temperature >= 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

hows_the_weather(68)

def fizzbuzz(num):
    if (num % 3) == 0 and (num % 5) == 0:
        # print ("FizzBuzz")
        return ("FizzBuzz")
    elif(num % 3) == 0: 
        # print("Fizz")
        return("Fizz")
    elif (num % 5) == 0:
        # print("Buzz")
        return ("Buzz")
    else:
        return(num)

fizzbuzz(15)
    

def calculator(operation, num1, num2):
    if operation == "+":
        # print (num1 + num2)
        return (num1 + num2)
    elif operation == "-":
        # print (num1 - num2)
        return (num1 - num2)
    elif operation == "*":
        return (num1 * num2)
    elif operation == "/":
        return (num1/num2)
    else:
        print("Invalid operation!")
        return None

calculator("/", 9, 3)
