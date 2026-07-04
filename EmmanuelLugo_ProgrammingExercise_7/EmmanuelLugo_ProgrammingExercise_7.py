

import re
#import re to access the built-in re module to use regular expressions.

# main(), executes other functions created to receive input and extract/display sentences
def main():

    #input received and stored in variable to be passed to other functions
    paragraph = input("Please enter a paragraph: ")

    #input passed in functions whose output will be stored in variables
    sentences = seperate_sentences(paragraph)

    #sentences passed into this function to display and calculate sentences
    display_sentence(sentences)

# function designed to take captured input by user and extract sentences
def seperate_sentences(paragraph):

    # Look ahead pattern to extract patterns.
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # used flags to makes sure sentences are captured correctly
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences


def display_sentence(sentence_list):
    for i in sentence_list:
        print(i)

    print(f"the total number of sentences is {len(sentence_list)}")


if __name__ == '__main__':
    main()