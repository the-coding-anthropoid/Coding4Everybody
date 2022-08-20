"""
Task:
     Rewrite autograder-03.3 using a function called computeGrade() that takes a 
     score as its parameter and returns a grade as a string.

Version:
    0.1.3
"""


def computeGrade(s) :
    """return a grade as a string based on a provided score

    param: s : float value of score

    return: str : grade calculated from score
    """
    if s > 1.0 or s < 0.0 :
        return "ERROR - value out of range."
    elif s >= 0.9 :
        return "Grade: A"
    elif s >= 0.8 :
        return "Grade: B"
    elif s >= 0.7 :
        return "Grade: C"
    elif s >= 0.6 :
        return "Grade: D"
    else :
        return "Grade: F"

def parseFloat(var) :
    """try to parse variable as float; exit with error message on fail

    param: var : variable to parse as float

    return: float : value of var on success
    """
    try :
        return float(var)
    except :
        print("ERROR - Input must be a number.")
        exit()


# prompt for score
score = parseFloat(input("Enter Score: "))
# print grade
print(computeGrade(score))


    


