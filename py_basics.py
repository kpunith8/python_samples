from math import ceil, sqrt
import random
import pdb
import datetime
import oop
import file_one
import string
# Regular expression module
import re

words = ["cat", "window", "defence"]

for word in words:
    print(word, len(word))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        # inserts an element to the words array by making a copy
        words.insert(0, w)

print(words)

print("Using range function:")
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

print("Fibobacci series: Creating functions")


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


fib(10)

print("String manipulation")
str1 = "Some academy"
print(str1.replace("Some", "Punith"))

print("Converting num to string, use str() function")
num = 10
print(str(num) + " is a number")

print("Math functions")
print("Power:", pow(5, 2), ",Ceiling", ceil(3.4), ",Sqaure root of 25", sqrt(25))
# Needs to import math
# use max(1, 2), min(10, 12) to find max and  min of 2 numbers
# round() rounds the value
# floor(3.2) -> 3
# ceil(3.4) -> 4
# sqrt(4) -> 2

# Read the values from keybard

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# To convert string to int, float() can be used to parse to float
# print("Hello", name + "!", "you are", int(age))

# Lists
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

# number tuple
number_tuple = (3, 4)

# inserting tuple to the list
mixed_list.insert(1, number_tuple)

print("Updated List: ", mixed_list)

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

# functions, passing arbitary arguments using
def arbitraryArguments(*names):
    for name in names:
        print("Hi", name)


arbitraryArguments("name1", "name2", "name3")

# Program to show the use of lambda functions
double = lambda x: x * 3

print("Calling lambda function:", double(5))

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

# Select only the words in a string starting with specific character
sample_str = "Secret agents are super good at staying hidden."
for word in sample_str.split():
    first_char = word.lower()[0]

    if first_char == "s":
        print(word)

first_char_of_a_word = [word[0] for word in sample_str.split()]
print("First character of a word in a sentence:", first_char_of_a_word)


def first_char_upper(str):
    return str[0].upper()


def last_two_chars(str):
    if len(str) < 2:
        return "Error: String is too small"
    else:
        return str[-2:]


def replace_and_switch(name):
    """
    Replaces any vowels in the name to x
    and switches the first char and last char
    """
    output = list(name)

    for i, letter in enumerate(name):
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            output[i] = "x"
        else:
            output[i] = letter

    last = output[-1]
    first = output[0]
    output[0] = last
    output[-1] = first

    return "".join(output)


# pdb.set_trace()  # stops here and allows interactively checking the return values of variables or functions

print("Capitalize first char of a string:", first_char_upper("unit"))
print("Last two char of a string:", last_two_chars("punith"))
print("Replace and switch chars:", replace_and_switch("Raghav"))


def square(num):  # function to pass it to map
    return num * num


print("map() to map each element in the list:", list(map(square, [1, 2, 3, 4, 5])))


def check_even(num):
    return num % 2 == 0


print(
    "filter() function returns the filtered list:",
    list(filter(check_even, [1, 2, 3, 4, 5, 6, 7, 8])),
)

print(datetime.date.today())
print(datetime.datetime.now())

# Using imported modules
circle = oop.Circle(10)
print("Area of circle:", circle.area(), " Perimeter:", circle.perimeter())

# use 'string' module to produce a list of lowercase letters
true_alphabet = list(string.ascii_lowercase)
random_alphabet = random.sample(true_alphabet, len(true_alphabet))

print(true_alphabet)
print(random_alphabet)

test_string = "This is a test string to apply regular expression Email:kpunith8@gmail.com no @handle"
pattern = r'[\w_.-]+@[\w_.-]+'

matched_email = re.search(pattern, test_string)

print('Email: found using regular expression', matched_email.group())

if __name__ == "__main__":
    print("py_basics.py is being run directly")
else:
    print("py_basics is being used by some other file")

# check the type of a variable
print("Type of words", type(words))