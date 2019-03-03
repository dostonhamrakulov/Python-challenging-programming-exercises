# Doston




## Question_1: ##
**Description:**

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

***Hints:***
Consider use range(#begin, #end, #step) method.

```python
numbers = range(2000, 3201)
sorted_numbers = []

for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        sorted_numbers.append(i)
print(sorted_numbers)
```
* * *

## Question_1: ##
**Description:**

Question:
Write a program which can compute the factorial of a given numbers.
Suppose the following input is supplied to the program:
8
Then, the output should be:

**Hints:**
In case of input data being supplied to the question, it should be assumed to be a console input.

**Solution 1:**
```python
user_in = input()
x = int(user_in)
b = 1
for a in range(1, x+1):
    b *= a
print(b)
```

**Solution 2:**
```python
def fact_2(x):
    if x == 0:
        return 1
    return x * fact_2(x - 1)

x=int(input())
print (fact_2(x))
```

