"""
Task:
    Write a program which prompts the user for a Celsius temperature, convert 
    the temperature to Fahrenheit, and print out the converted temperature.

Formula:
    (C * 9 / 5) + 32 = F

Version:
    0.1.1
"""

# prompt
print(  "Please enter a temperature in Celsius you would like converted to" +
        "Fahrenheit.")
print(  "Celsius:", end=' ')
celsius = input()
# conversion
fahrenheit = (float(celsius) * 9 / 5 ) + 32
# output
print(  "Fahrenheit: " + str(fahrenheit))