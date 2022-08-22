"""
Task:
    Write a program that reads a file and prints the letters in decreasing order 
    of frequency. Your program should convert all the input to lower case and 
    only count the letters a-z. Your program should not count spaces, digits, 
    punctuation, or anything other than the letters a-z. Find text samples from 
    several different languages and see how letter frequency varies between 
    languages.

    0.2.1
"""

# load file
while True:
    file = input("Enter file name: ")
    try:
        fhandle = open(file)
        break
    except:
        print("Could not find file, please try again...")

# get apha characters from file
count = {}
totalChars = 0
for line in fhandle:
    for character in line:
        if character.isalpha():
            totalChars += 1
            character = character.lower()
            count[character] = count.get(character, 0) + 1

# sort and print freq
orderedFrequency = sorted( [ (let, freq) for let, freq in count.items()])
for let, freq in orderedFrequency:
    percent = "{:.3%}".format(freq/totalChars)
    print(let, percent)
