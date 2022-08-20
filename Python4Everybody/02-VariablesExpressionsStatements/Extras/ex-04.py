"""
Task:
    Assuming the following assignment statements:
        width = 17
        height = 12.0
    Write the value of the expression and the type (of the value of the 
    expression) for each of the following:
        width//2
        width/2.0
        height/3
        1 + 2 * 5

Version:
    0.4.1
"""

# dictated assignments
width = 17
height = 12.0


def test (expressionValue, predictedValue, predictedType):
    """Tests an expression for it's evaluated value and type of the value

    :param expressionValue: expression to be tested
    :param predictedValue: predicted value of expression
    :param predictedType: predicted type of expression (<class> 'type')
    """
    print(  "Expression:\t\t" + str(expressionValue))
    print(  "Predicted Value:\t" + str(predictedValue) + 
            "\t\tPredicted Type:\t" + (predictedType))
    print(  "Actual Value:\t\t" + str(expressionValue) + 
            "\t\tActual Type:\t" + str(type(expressionValue)))

    if (    expressionValue == predictedValue and 
            str(type(expressionValue)) == predictedType) :
        print("CORRECT!")
    else :
        print ("WRONG!")

    print()


#output
print("width = " + str(width))
print("height = " + str(height))
print()
test((width//2), "width//2", 8, "<class 'int'>")
test((width/2.0), "width/2.0", 8.5, "<class 'float'>")
test((height/3), "height/3", 4.0, "<class 'float'>")
# this is wrong; type is int; wasn't sure - but 11 is int (duh)
test((1 + 2 * 5), "1 + 2 * 5", 11, "<class 'float'>")