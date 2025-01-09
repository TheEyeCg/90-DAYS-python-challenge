#!/usr/bin/env python3

print ("create a program that takes input for their name and age,then print a greeting with their name and calculates the year they were born")
#input user name and age
name= input("enter your name: ")
age= input ("enter your age: ")

#change age to integer
age= int(age)

#calculate year of birth
current_year= 2025
year_of_birth= current_year - age

#greetings

print (f"hi {name} hope you see christ is working?, you're born in the year {year_of_birth}")
