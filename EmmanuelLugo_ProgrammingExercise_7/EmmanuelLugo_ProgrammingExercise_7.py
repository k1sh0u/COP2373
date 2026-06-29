'''
Using the code in Section 7.4, write a program that will allow me to enter a paragraph, including sentences which begin with numbers. Display each individual sentence and the count of sentences in the paragraph.

You should have at least two functions, but you could have more.



okay so we have to use re.findall, i'm assuming.


pseudo code;

def main:




def capture_sentence():
    this will capture the raw sentence


def seperate_sentence():
    this function will seperate each sentence, maybe at a period.?"




'''

import re

def main():

    paragraph = input("Please enter a paragraph: ")

    sentences = seperate_sentences(paragraph)
    display_sentence(sentences)


def seperate_sentences(paragraph):
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences

def display_sentence(sentence_list):
    for i in sentence_list:
        print(i)

    print(f"the total number of sentences is {len(sentence_list)}")


if __name__ == '__main__':
    main()