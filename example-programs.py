import random
import re
import string

# use 'string' module to produce a list of lowercase letters
true_alphabet = list(string.ascii_uppercase)
random_alphabet = random.sample(true_alphabet, len(true_alphabet))

print('List of alphabets:', true_alphabet)
print('List of random alphabets:', random_alphabet)


# Regular expressions
test_string = "This is a test string to apply regular expression Email:kpunith8@gmail.com no @handle"
pattern = r'[\w_.-]+@[\w_.-]+'

matched_email = re.search(pattern, test_string)

print('Email found using regular expression', matched_email.group())

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

# Add the method docs with """ quotes


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


print("map(): to map each element in the list:",
      list(map(square, [1, 2, 3, 4, 5])))


def check_even(num):
    return num % 2 == 0


print(
    "filter(): function returns the filtered list:",
    list(filter(check_even, [1, 2, 3, 4, 5, 6, 7, 8])),
)
