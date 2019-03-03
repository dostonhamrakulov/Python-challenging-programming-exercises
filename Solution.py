


# =========================   Question_1: ===========================================
# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5,
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
# In case of input data being supplied to the question, it should be assumed
# to be a console input.

def fact_1(x):
    b = 1
    for a in range(1, x+1):
        b *= a
    return b
print("Exercise_2: Solution_1(input like 8 or 9)")
# x = int(input())
# print(fact_1(x))


# Solution 2:
def fact_2(x):
    if x == 0:
        return 1
    return x * fact_2(x - 1)

print("Exercise_2: Solution_2(input like 8 or 9)")
# x=int(input())
# print (fact_2(x))


# =========================   Question_3: ===========================================
# Question:
# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a
# console input.
# Consider use dict()

def prog_1(x):
    dict_ = dict()
    for a in range(1, x+1):
        dict_[a] = a*a
    print(dict_.__str__())
print("Exercise_3: input like 8, 7 or 9")
# prog_1(int(input()))

# =========================   Question_4: ===========================================
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a
# console input.
# tuple() method can convert list to tuple

print("Exercise:4 (input like 30,23,24,345)")
def prog_2():
    x = input()
    l = []
    for a in x.split(","):
        l.append(a)
        print(x)
    t = tuple(l)
    print(l)
    print(t)
# prog_2()


# =========================   Question_5: ===========================================
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters

class Class_1:
    def __init__(self, str_):
        self.str_ = str_

    def getString(self):
        print("Enter string:")
        self.str_ = input()
        return
    def printString(self):
        return print(self.str_)

x = Class_1("Salom, Doston")
x.printString()


# =========================   Question_6: ===========================================
# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


def two_dimens_arr(x, y):
    l1 = []
    for a in range(x):
        l1.append([])
        for b in range(y):
            d = a * b
            l1[a].append(a*b)
    print(l1)
    return
two_dimens_arr(4, 4)


# =========================   Question_7: ===========================================
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def prog_3():
    x = input()
    list_ = []

    for a in x.split(","):
        list_.append(a)
    list_.sort()
    str_ = ",".join(list_)
    print(list_)
    print(str_)
    return
