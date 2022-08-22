"""
Task:
    Write a program that prompts the user for a list of numbers and prints out 
    the maximum and minimum of the numbers at the end when the user enters 
    “done”. Write the program to store the numbers the user enters in a list and 
    use the max() and min() functions to compute the maximum and minimum numbers 
    after the loop completes.

version:
    0.1.1
"""

# create list to store values
lst = list()

# data collection loop
while True :
    # prompt
    num = input("Enter a number: ")
    # done check
    if num == "done" : break
    # error handling
    try:
        num = float(num)
    except:
        print("ERROR - input must be a numeric characters or 'done' when done")
        continue
    # add number to list
    lst.append(num)

# output
print("Maximum:", max(lst))
print("Minimum:", min(lst))