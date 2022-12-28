#!/usr/bin/env python3

# Created by: Kent G
# Date: Dec.15, 2022
# This program parses the user's string
# and prints each word on a new line


def string_parser(unparsed_string):

    # Returns the average of all marks in the list
    return unparsed_string.split()


def main():

    # Gets the user's sentence
    user_string = input("Enter a string: ")

    # Stores the parsed sentence in words variable
    words = string_parser(user_string)

    # Prints each word on a new line
    for counter in words:
        print(f"{counter}\n")


if __name__ == "__main__":
    main()
