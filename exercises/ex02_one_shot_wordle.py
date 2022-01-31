"""EX02 - One Shot Wordle."""

__author__ = "730425241"

secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
playing: bool = True
guess: str = input("What is your 6-letter guess? ")
i: int = 0
r: str = ""

while playing:
    if len(guess) != 6:
        guess = input("That was not 6 letters! Try again: ")
    elif guess == secret:
        while i < len(guess):
            if guess[i] == secret[i]:
                r = r + GREEN_BOX
            i = i + 1
        print(r)
        print("Woo! You got it!")
        playing = False
    else:
        guess != secret
        while i < len(guess):
            if guess[i] == secret[i]:
                r = r + GREEN_BOX
            else:
                exists: bool = False
                a: int = 0
                while exists is not True and a < len(guess):
                    if secret[a] == guess[i]:
                        exists = True
                    else:
                        a = a + 1
                if exists is True:
                    r = r + YELLOW_BOX
                else:
                    r = r + WHITE_BOX
            i = i + 1
        print(r)
        print("Not quite. Play again soon!")
        playing = False
