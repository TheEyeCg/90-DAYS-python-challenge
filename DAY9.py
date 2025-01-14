#!/usr/bin/env python3
print("Error handling")
print("TASK: Create a program that takes user input for a number and catches errors if the user inputs something invalid (non-integer)")
print("---------------------------------------------------------------------------------------------------")

# Ask for user input
user_input = input("Enter a number: ")

try:
    # Attempt to convert the input to an integer
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Error: Invalid input. Please enter a valid integer.")
