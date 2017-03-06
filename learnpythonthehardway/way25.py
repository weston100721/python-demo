#!/usr/bin/python
# -*- coding: UTF-8 -*-


def break_words(stuff):
    """
this function will break up words for us.
    :param stuff: the import sentence.
    :return:
    """
    words = stuff.split(' ')
    return words


def sort_words(words1):
    """
sorts the words.
    :param words1:
    :return:
    """
    return sorted(words1)


def print_first_word(words2):
    word = words2.pop(0)
    print word


def print_last_word(words3):
    """Prints the last word after popping it off."""
    word = words3.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


if __name__ == '__main__':
    string = "Takes in a full sentence and returns the sorted words."
    words = sort_sentence(string)
    print words
    print_first_and_last_sorted(string)