


# =========================   Question_1: ===========================================
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method


numbers = range(2000, 3201)
sorted_numbers = []

for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        sorted_numbers.append(i)
print(sorted_numbers)




# =========================   Question_2: ===========================================

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def fact_1(x):
    b = 1
    for a in range(1, x+1):
        b *= a
    return b
x = int(input())
print(fact_1(x))


# Solution 2:
def fact_2(x):
    if x == 0:
        return 1
    return x * fact_2(x - 1)

x=int(input())
print (fact_2(x))


# =========================   Question_2: ===========================================
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

def prog_1(x):
    dict_ = dict()
    for a in range(1, x+1):
        dict_[a] = a*a
    print(dict_.__str__())
prog_1(int(input()))
