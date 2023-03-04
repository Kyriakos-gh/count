# count.py: Counts the number of lines and words in a text file.
# Usage: count.py filename
# You can also execute it with out an argument and to give the filename in the program execution. 
# Kyriakos, 4/3/2023

import sys

def count_lines_words(filename):
    """Counts the lines and words in a file."""
    try:
        with open(filename, encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    else:
        lines_num = len(lines)
        words_num = 0
        for line in lines:
            words = line.split()
            words_num += len(words)
        print(f"The file {filename} has {lines_num} lines and {words_num} words.")

if len(sys.argv) != 2:
    try:
        filename = input("Please enter the name of the text file to count for lines and words: ")
    except KeyboardInterrupt:
        print("\nExit requested.")
        sys.exit(0)
    else:
        count_lines_words(filename)
else:
    count_lines_words(sys.argv[1])