"""
Task:
    Write a program that uses input to prompt a user for their name and then 
    welcomes them.

Version:
    0.2.0
"""

# prompt user for name; replace '\n' with ' ' for single line prompt
print("Please enter your name:", end=' ')
# store user input in variable 'name'
name = input()
# print string literal and name variable as one concatenated string
print("Welcome, " + name)