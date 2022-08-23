# Python 4 Everyone

## 11 - Regular Expressions

### Python Regular Expression Quick Guide


<table>
<tr>
<td>
<img width="200px" height="1px"><br>
<bold> ^ </bold>
</td>
<td >
<img width="600px" height="1px"><br>
<em>Matches the beginning of a line</em>
</td>
</tr>
<tr>
<td><bold> $ </bold></td>
<td><em>Matches the end of the line</em></td>
</tr>
<tr>
<td><bold> . </bold></td>
<td>M<em>atches any character</em></td>
</tr>
<tr>
<td><bold> \s </bold></td>
<td>M<em>atches whitespace</em></td>
</tr>
<tr>
<td><bold> \S </bold></td>
<td><em>Matches any non-whitespace character</em></td>
</tr>
<tr>
<td><bold> * </bold></td>
<td><em>Repeats a character zero or more times</em></td>
</tr>
<tr>
<td><bold> *? </bold></td>
<td><em>Repeats a character zero or more times (non-greedy)</em></td>
</tr>
<tr>
<td><bold> + </bold></td>
<td><em>Repeats a character one or more times</em></td>
</tr>
<tr>
<td><bold> +? </bold></td>
<td><em>Repeats a character one or more times (non-greedy)</em></td>
</tr>
<tr>
<td><bold> [aeiou] </bold></td>
<td><em>Matches a single character in the listed set</em></td>
</tr>
<tr>
<td><bold> [a-z0-9] </bold></td>
<td><em> The set of characters can include a range</em></td>
</tr>
<tr>
<td><bold> ( </bold></td>
<td>I<em>Indicates where string extraction is to start</em></td>
</tr>
<tr>
<td><bold> ) </bold></td>
<td><em>Indicates where string extraction is to end</em></td>
</tr>
</table>
         
<br>  

The repeat characters (__*__ and __+__) push outward in both directions to match the largest possible string as standard - this is 'greedy matching'.

Non-greedy matching suppresses this behaviour, resulting in the earliest possible match.

#### Example

```python
# greedy
print(re.findall("^F.+:", "From: Queen Victoria: Empress of Britannia")
>>> ['From: Queen Victoria:']

# non-greedy
print(re.findall("^F.+?:", "From: Queen Victoria: Empress of Britannia")
>>> ['From:']
```