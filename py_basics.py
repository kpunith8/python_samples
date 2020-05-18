from math import ceil, sqrt
import random
import pdb
import datetime

# User defined imports, import by file-name
import oop
import file_one

# Functions
print("Fibobacci series")


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


fib(10)

# Functions, passing arbitrary arguments


def arbitraryArguments(*names):
    for name in names:
        print("Hi", name)

print('Function accepting arbitrary number of arguments, *Operator:')
arbitraryArguments("name1", "name2", "name3")

# Lambda functions


def double(x): return x * 3


print("Lambda functions:", double(5))

# Strings
print("String manipulation")
str1 = "Some academy"
print(str1.replace("Some", "Punith"))

print("Converting num to string, use str() function")
num = 10
print(str(num) + " is a number")
print('in() to check the presence of a word in a string:', "Some" in str1)

# Math Functions

# print("Math functions")
# print("Power:", pow(5, 2), ",Ceiling", ceil(
#     3.4), ",Sqaure root of 25", sqrt(25))
# Needs to import math
# use max(1, 2), min(10, 12) to find max and  min of 2 numbers
# round(value) rounds the value, abs(value)
# floor(3.2) -> 3
# ceil(3.4) -> 4
# sqrt(4) -> 2


# Read the values from keybard

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# To convert string to int, float() can be used to parse to float
# print("Hello", name + "!", "you are", int(age))

# Lists
words = ["cat", "window", "defence"]

for word in words:
    print(word, len(word))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        # inserts an element to the words array by making a copy
        words.insert(0, w)

print('Insert an item to list:', words)

print("Using range function:")
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

lucky_numbers = [23, 12, 44, 32, 99]
friends = ["abc", "abd", "tbd"]

# Getting the range from the list
# can be specified as follows(2:) - from position 2 to end of the list; (:4) - from 0th element to 3rd element
print(lucky_numbers[:4])

# Extending the list
# list.append('item') - to add new items to the end of list
friends.extend(lucky_numbers)
# insert(index, item) to insert item at specified position
friends.append("oof")
friends.insert(3, "lss")
print(friends)

mixed_list = [{1, 2}, [5, 6, 7]]

# Tuples

# number tuple
number_tuple = (3, 4)

# inserting tuple to the list
mixed_list.insert(1, number_tuple)

print("Updated List: ", mixed_list)

# unpacking a tuple or a list
item1, item2 = number_tuple
item3, item4 = [33,22]

print('Unpacking an tuple or list:', item1, item2, item3, item4)

# Calculate the sum of each digit


def sumDigit(num):
    sum = 0
    while num:
        sum += num % 10
        num = int(num / 10)
    return sum


# using max(arg1, arg2, *args, key)
print("Maximum is:", max(100, 321, 267, 59, 40, key=sumDigit))

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print("Maximum is:", max(num, key=sumDigit))

# random list
randomList = ["a", ("a", "b"), [3, 4]]

# element ('a', 'b') is searched
index = randomList.index(("a", "b"))

# index is printed
print("The index of ('a', 'b'):", index)

# element [3, 4] is searched
index = randomList.index([3, 4])

# index is printed
print("The index of [3, 4]:", index)

# take second element for sort


def takeSecond(elem):
    return elem[0]


# random list
randomList = [(2, 2), (3, 4, 5), (4, 1, 6, 7), (1, 3)]

# sort list with key
randomList.sort(key=takeSecond)

# print list
print("Sorted list using a key:", randomList)
# Sort based on length of the elements
sorted(randomList, key=len)

print("Sorted list using length of the list", randomList)

print("Sets will have unique values", {1, 2, 3, 2, 1, 2, 1})

print("Tuples can be specified in () and are immutable", (1, 2, 3))

# Dictionary is an unordered collection of key-value pairs.

d = {"key": 1, "value": 2, "list": [1, 2, 3]}
print("type of d", type(d))

print("d['key'] = ", d["key"])

print("d['list'] = ", d["list"])

print(d.keys(), d.values())

# Formatting with print()
print("I love {0} and {1}".format("bread", "butter"))
# Output: I love bread and butter

print("I love {1} and {0}".format("bread", "butter"))
# Output: I love butter and bread

# The actual syntax of the print() function is

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1, 2, 3, 4)

print(1, 2, 3, 4, sep="*")

print(1, 2, 3, 4, sep="#", end="&")

print("Hello {name}, {greeting}".format(greeting="Goodmorning", name="John"))

print("Format floating number {:.2f}".format(234.333232))

d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(d[key])

list1 = ["a", "b", "c", "e"]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Creating a list of tuples using zip():", list(zip(list1, list2)))

print("min('xmsabc'):", min("xmsabc"), ", max('xmsabc'):", max("xmsabc"))
# print("Using shuffle:", shuffle(list1))

squares = [x ** 2 for x in range(1, 10)]
print("List of sqaures using list comprehension", squares)

even_numbers = [x for x in range(1, 10) if x % 2 == 0]
print("List of even numbers using list comprehension", even_numbers)


## Date and Time
print(datetime.date.today())
print(datetime.datetime.now())


# Using imported modules
circle = oop.Circle(10)
print("Area of circle:", circle.area(), " Perimeter:", circle.perimeter())

person = oop.Agent('Punith', 'black', 165)
print('Person details', person, person.report())


if __name__ == "__main__":
    print("py_basics.py is being run directly")
else:
    print("py_basics is being used by some other file")

# Arithmetic operations on floting point numbers
floatDiv = 10 / 3 # returns 3.3333333...
floatDivAbsolute = 10 // 3 # returns 3, truncating the decimals
exponentOf3 = 3 ** 3 # returns 27

iterStar = 1
while iterStar <= 5:
    print("*" * iterStar)
    iterStar += 1