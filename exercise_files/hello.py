#!/usr/bin/python3
# This program prints hello world to the screen
import sys

from termcolor import colored, cprint

text = colored("Hello, world!", "red", "on_white")
print(text)
