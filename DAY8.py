#!/usr/bin/env python3

def count_lines_and_words(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")

    except FileNotFoundError:
        print("The file was not found. Please check the filename.")
my_file= "lina.txt"
count_lines_and_words (my_file)