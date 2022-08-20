"""
Task:
    Rewrite your pay program from autograder-03.1 using try and except so that 
    it handles non-numeric input gracefully by printing a message and exiting 
    the program.

Version:
    0.1.1
"""

def toNumber(var) :
    """checks if a value can be parsed as a float; if not prints an error message 
    and exits program

    :param var : the value to check

    :return float : var typecast to float
    """
    try :
        v = float(var)
        return v
    except :
        print("Please enter a numeric value")
        exit()

# hours prompt
print("Enter hours worked:", end=' ')
hours = toNumber(input())

# rate prompt
print("Enter hourly rate of pay:", end=' ')
rate = toNumber(input())

# pay calculation
if hours > 40 :
    pay = (40 * rate) + (hours - 40) * (rate * 1.5)
else :
    pay = hours * rate

# output
print("Pay: " + str(pay))


