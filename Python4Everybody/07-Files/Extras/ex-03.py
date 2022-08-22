"""
Task:
     Sometimes when programmers get bored or want to have a bit of fun, they add 
     a harmless Easter Egg to their program. Write a program that prompts the 
     user for the file name so that it prints a funny message when the user 
     types in the exact file name “na na boo boo”. The program should count 
     subject lines for all other files which exist and exit with an error 
     message for files that don't.

Version:
    0.1.5
"""
# prompt for file name
fileName = input("Enter the file name: ")

# check file exists
try:
    fhand = open(fileName)
except:
    # easter egg
    if fileName == "na na boo boo" :
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    # error message
    else :
        print("File cannot be opened:", fileName)
    exit()

count = 0

# count subject lines
for line in fhand :
    if line.startswith("Subject: ") :
        count += 1

# output
print("There were", count, "subject lines in", fileName)