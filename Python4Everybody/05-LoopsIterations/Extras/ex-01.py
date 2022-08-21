"""
Task:
     Write a program which repeatedly reads numbers until the user enters 
     “done”. Once “done” is entered, print out the total, count, and average of 
     the numbers. If the user enters anything other than a number, detect their 
     mistake using try and except and print an error message and skip to the 
     next number.

Version:
    0.3.1
"""

runningTotal = 0
inputCount = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("ERROR: program requires numeric input, or 'done' when done")
        continue
    inputCount += 1
    runningTotal += num

meanAverage = runningTotal/inputCount

print("The total of the numbers in the data set is:\t", runningTotal)
print("The count of numbers in the data set is:\t", inputCount)
print("The mean average for the data set is:\t\t", meanAverage)