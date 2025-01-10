#!/bin/usr/env python3
from operator import add


def greet():
    print("hello love")
#calling the function
name= input ( "eneter your name: ")
def greet(name):

#define a function with returned value
 def add(a, b):
    return a + b

result = add(5, 3)
print ("sum:" ,result)

x = 10  # Global variable

def show():
    y = 5  # Local variable
    print("Inside function:", x + y)

show()
print("Outside function:", x)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Testing the function
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
