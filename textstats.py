"""Program which takes a text document and returns various statistics with
an interactive user interface"""

import sys


def analyze_text(argv):
    """Repeatable function which opens a text file given as an argument,
    initializes a dictionary to keep track of statistics, then opens the file
    and iterates through each line, then each word. If the word exists as a key
    already in the dictionary, one is added to the count of its appearance,
    if not then a new key/value pair is added with an initial value of 1.
    Simultaneously total number of lines and words are tracked and reported
    The function returns a combined dictionary with a count for each word of
    total appearances, and appearances at the beginning and end of a sentence"""
    # dictionary containing {word: count} to track all words
    words = {}
    # dictionary containing {word: count} to track words beginning a sentence
    beginning = {}
    # dictionary containing {word: count} to track words ending a sentence
    end = {}
    # bool to track beginning of new sentence
    # starts true because the beginning of the file is a new sentence
    new_sentence = True
    num_lines = 0
    num_words = 0
    punctuation = [".", "?", "!"]

    with open(argv[1], mode='r', encoding='utf-8') as file:
        for line in file:
            # iterate line count
            num_lines += 1
            for word in line.split():
                # iterate word count
                num_words += 1
                # clean current word (without removing punctuation)
                word = clean_word(word)

                if new_sentence:
                    beginning = add_word(word, beginning)
                    new_sentence = False

                for item in punctuation:
                    # if it's at the end it's the end of a sentence
                    if word[-1] == item:
                        word = word.strip(item)
                        end = add_word(word, end)
                        new_sentence = True
                        # break for efficiency
                        break

                    # if it's in the middle it's a space missing after a period
                    # don't need to touch new_sentence because that's
                    # dealt with inside this loop
                    if item in word:
                        piece = word.split(item)
                        words = add_word(piece[0], words)
                        words = add_word(piece[1], words)
                        end = add_word(piece[0], end)
                        beginning = add_word(piece[1], beginning)
                        # continue so these words don't get added twice
                        continue

                # add all words to primary tracker
                words = add_word(word, words)

    print(f"Text document {argv[1]} analyzed. \n\t" +
          f"Total number of lines: {num_lines}" +
          f"\n\tTotal number of words: {num_words}")

    # Create final dictionary combining relevant information
    analysis = combine_dicts(words, beginning, end)
    return analysis


def clean_word(word):
    """function for cleaning up a word by making it lowercase,
    and removing useless characters and empty space"""
    to_strip = [",", ")", "(", '"', "'", "@", "#", "$", "%",
                "^", "&", "*", "<", ">", ":", ";"]
    word = word.lower()
    for item in to_strip:
        word = word.replace(item, '')
    word = word.strip()
    return word


def combine_dicts(words, beginning, end):
    """function for combining all three dictionaries with word: count
    into a single one with word: [total count, beginning count, end count]"""
    analysis = {}
    for word, value in words.items():
        # Appearance in words, beginning, then end
        values = [value, 0, 0]
        if word in beginning:
            values[1] = beginning[word]
        if word in end:
            values[2] = end[word]
        analysis[word] = values
    return analysis


def add_word(word, dict_to_edit):
    """function for adding word to any dictionary"""
    if word in dict_to_edit:
        dict_to_edit[word] += 1
    else:
        dict_to_edit[word] = 1
    return dict_to_edit


result = analyze_text(sys.argv)
print("Enter a word at the prompt to see its statistics.\n")

user_input = input("Enter a word or type quit: ")
while user_input.lower() != "quit":
    try:
        print(f"Statistics for the word {user_input}" +
              f"\n\tTotal Appearance count: {result[user_input][0]}" +
              f"\n\tCount at Beginning of Sentence: {result[user_input][1]}" +
              f"\n\tCount at End of Sentence: {result[user_input][2]}\n")
    except KeyError:
        print("Error: Word not in file")
    user_input = input("Enter a word or type quit: ")
print("Thank you for using the program! Quitting..")
