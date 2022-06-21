"""Program to check for existence of a palindrome"""

import sys
import string


def check_palindrome(argv):
    """Repeatable function to check for palindrome which first strips
    the given input of punctuation, spaces, and makes it lowercase,
    then simply returns a boolean by comparing the word to itself in reverse
    without the need to iterate through each character, or save a second
    variable"""
    given_word = argv[1].translate(str.maketrans('', '', string.punctuation))
    given_word = (given_word.replace(' ', '')).lower()
    return print(given_word == given_word[::-1])


# Call function
check_palindrome(sys.argv)
