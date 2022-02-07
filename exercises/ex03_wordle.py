"""EX03 - Wordle."""

__author__ = "730425241"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    secret: str = "codes"
    N: int = 1
    won: bool = False
    while N <= 6 and won is False:
        print("=== Turn " + str(N) + "/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
            print("You won in " + str(N) + "/6 turns!")
        else:
            N += 1
    if N > 6:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(a: str, b: str) -> bool:
    """Determines if character is found in a."""
    assert len(b) == 1
    i: int = 0
    exists: bool = False
    while i < len(a):
        if b == a[i]:
            exists = True
        i += 1
    if exists is True:
        return True
    if exists is False:
        return False


def emojified(guess: str, secret: str) -> str:
    """Determines which colored boxes the guess and secret align to."""
    assert len(guess) == len(secret)
    i: int = 0
    r: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            r += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            r += YELLOW_BOX
        else:
            r += WHITE_BOX
        i += 1
    return r 


def input_guess(expected_length: int) -> str:
    """Determines the expected length of the guess."""
    e: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(e) != expected_length:
        e = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return e


if __name__ == "__main__":
    main()