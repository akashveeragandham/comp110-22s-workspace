"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730425241"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    exit("Error: Word must contain 5 characters")
else:
    character: str = input("Enter a single character: ")
    if len(character) != 1:
        exit("Error: Character must be a single character.")
    else:
        print("Searching for " + character + " in " + word)

if character == word[0]:
    print(character + " found at index 0")
if character == word[1]:
    print(character + " found at index 1")
if character == word[2]: 
    print(character + " found at index 2")
if character == word[3]: 
    print(character + " found at index 3")
if character == word[4]:
    print(character + " found at index 4")