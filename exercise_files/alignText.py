#!/usr/bin/python3
# Print given string in the centre
# Author: Rishi Kapoor
# Date: 26.01.2023
import os
term_width=os.get_terminal_size().columns

string=input("Enter the string: ")
print(string.center(term_width))
print(string.ljust(term_width))
print(string.rjust(term_width))
