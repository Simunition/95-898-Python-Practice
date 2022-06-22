"""Program which takes a text document and returns various statistics"""

import sys


def analyze_text(argv):
    """Repeatable function which opens a text file given as an argument,
    initializes a dictionary to keep track of statistics, then opens the file
    and iterates through each line, then each word. If the word exists as a key
    already in the dictionary, one is added to the count of its appearance,
    if not then a new key/value pair is added with an initial value of 1.
    Simultaneously total number of lines and words are tracked and reported"""
    words = {} # dictionary containing {word: count} to track all words
    beginning = {} # dictionary containing {word: count} to track words beginning a sentence
    end = {} # dictionary containing {word: count} to track words ending a sentence
    new_sentence = True # bool to track beginning of new sentence
                        # starts true because the beginning of the file is a new sentence
    num_lines = 0
    num_words = 0
    punctuation = ["?", "!", "."]
    to_strip = [",", ")", "(", '"', "'", "@", "#", "$", "%", "^", "&", "*", "<", ">", ":", ";", " "]

    with open(argv[1], mode='r', encoding='utf-8') as file:
        for line in file:
            num_lines +=1
            for word in line.split():
                num_words += 1
                # clean up word by making it lowercase, and removing useless characters
                word = word.lower()
                for item in to_strip:
                    word = word.replace(item, '')

                # Loop for populating end if the word contains punctuation,
                # and indicating new sentence
                if any(item in word for item in punctuation): #if word contains punctuation
                    # Remove puctuation and add word to end
                    for item in punctuation:
                        word = word.replace(item, '')
                    new_sentence = True
                    if word in end:
                        end[word] += 1
                    else:
                        end[word] = 1

                # Loop for populating beginning if new_sentence is true
                if new_sentence:
                    if word in beginning:
                        beginning[word] += 1
                    else:
                        beginning[word] = 1
                    new_sentence = False

                # Core functinoality, adds each word to the primary word tracker
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

    print(f"Text document {argv[1]} analyzed. \n\tTotal number of lines: {num_lines}" +
            f"\n\tTotal number of words: {num_words}")

    # Create final dictionary combining relevant information

    return words # Needs to return multiple dictionaries...


result = analyze_text(sys.argv)
print("Enter a word at the prompt to see its statistics.\n")

user_input = input("Enter a word or type quit: ")
while user_input.lower() != "quit":
    try:
        print(f"Statistics for the word {user_input}" +
                f"\n\tcount: {result[user_input]}")
    except KeyError:
        print("Error: Word not in file")
    user_input = input("Enter a word or type quit: ")
print("Thank you for using the program! Quitting..")
