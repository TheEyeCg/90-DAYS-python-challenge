#!/usr/bin/env python3
import json

# Load data from a JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Ask user for a key to retrieve
key = input("Enter the key you want to retrieve: ")

# Print the value or an error message
print(data.get(key, "Key not found."))
