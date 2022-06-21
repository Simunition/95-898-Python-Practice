"""Program to take two command line arguments, a word and a number and
rotate the word that number of times"""

import sys


def rotate(argv):
    """Function to take arguments and rotate word"""
    word = argv[1]
    num_times = int(argv[2])
    return print(word[num_times:] + word[:num_times])


# Call function
rotate(sys.argv)
