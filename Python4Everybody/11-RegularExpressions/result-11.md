# Python 4 Everyone

## 11 - Regular Expressions

### Videos

- [Regular Expressions - Part 1](https://youtu.be/ovZsvN67Glc)
- [Regular Expressions - Part 2](https://youtu.be/fiar4QZZ7Xo)
- [Regular Expressions - Part 3](https://youtu.be/GiQdXo2Bvgc)


### Slides

- [Powerpoint](../Resources/Pythonlearn-11-Regex.pptx)

### References

- [www.py4e.com](https://www.py4e.com/html3/11-regex)
- [Regex Quick Guide](regex.md)

### Assignments

#### Autograder: Regular Expressions

```python
import re

# load file
while True:
    file = input("Please enter filename: ")
    try:
        fhandle = open(file)
        break
    except:
        print("Could not find file", file)

# find and sum numbers
total = 0

for line in fhandle:
    nums = re.findall('[0-9]+', line)
    for num in nums:
        total += int(num)

print(total)
```

![Image of Grade for Autograder Assignment: Regular Expressions](./grade-regex.png)


#### Quiz

<!-- ![Image of quiz Assignment](quiz-11.png) -->

