"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730425241"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

matches: int = 0

if character == word[0]:
    print(character + " found at index 0")
    matches = matches + 1
if character == word[1]:
    print(character + " found at index 1")
    matches = matches + 1
if character == word[2]: 
    print(character + " found at index 2")
    matches = matches + 1
if character == word[3]: 
    print(character + " found at index 3")
    matches = matches + 1
if character == word[4]:
    print(character + " found at index 4")
    matches = matches + 1

if matches == 1:
    print(str(matches) + " instance of " + character + " found in " + word)
else:
    if matches > 1:
        print(str(matches) + " instances of " + character + " found in " + word)
    else: 
        print("No instances of " + character + " found in " + word)
