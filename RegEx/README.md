# Python Programming Exercise - Regular Expressions

### Description:
Here I try to make list of regular expression questions and answer for them.

### Note:
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

### Programming languages and frameworks
```python
Python, Vim
```

### IDE
```python
PyCharm
```

## Author
**Doston Hamrakulov**
>*Software Engineer, Web Developer, Freelancer*


## This set of Python Multiple Choice Questions & Answers (MCQs) focuses on “Regular Expressions”.

## Question_1: Which module in Python supports regular expressions? ##
Question:
```python
a) re
b) regex
c) pyregex
d) none of the mentioned
```
Answer:
```python
Answer: a
Explanation: re is a part of the standard library and can be imported using: import re.
```
* * *

## Question_2: Which of the following creates a pattern object? ##
Question:
```python
a) re.create(str)
b) re.regex(str)
c) re.compile(str)
d) re.assemble(str)
```
Answer:
```python
Answer: c
Explanation: It converts a given string into a pattern object.
```
* * *

## Question_3: What does the function re.match do? ##
Question:
```python
a) matches a pattern at the start of the string
b) matches a pattern at any position in the string
c) such a function does not exist
d) none of the mentioned
```
Answer:
```python
Answer: a
Explanation: It will look for the pattern at the beginning and return None if it isn’t found.
```
* * *

## Question_4: What is the output of the following? ##
Question:
```python
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())
```

```python
a) (‘we’, ‘are’, ‘humans’)
b) (we, are, humans)
c) (‘we’, ‘humans’)
d) ‘we are humans’
```
Answer:
```python
Answer: a
Explanation: This function returns all the subgroups that have been matched
```
* * *
## Question_5: What does the function re.search do? ##
Question:
```python
a) matches a pattern at the start of the string
b) matches a pattern at any position in the string
c) such a function does not exist
d) none of the mentioned
```
Answer:
```python
Answer: b
Explanation: It will look for the pattern at any position in the string.
```
* * *

## Question_6: What is the output of the following? ##
Question:
```python
sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())
```
s
```python
a) {‘animal’: ‘horses’, ‘verb’: ‘are’, ‘adjective’: ‘fast’}
b) (‘horses’, ‘are’, ‘fast’)
c) ‘horses are fast’
d) ‘are’
```
Answer:
```python
Answer: a
Explanation: This function returns a dictionary that contains all the matches.
```
* * *
