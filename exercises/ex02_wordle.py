"""Can you guess the secret word?"""

__author__: str = "730469891"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    guess: str = ""
    while turns <= 6 and guess != secret:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
        else:
            turns += 1
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(answer: str, letter: str) -> bool:
    """Is the letter in the word?"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    count: int = 0
    while count < len(answer):
        if answer[count] == letter:
            return True
        else:
            count += 1
    return False


def emojified(guess: str, answer: str) -> str:
    """Actually displays the boxes."""
    assert len(guess) == len(answer), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    display: str = ""
    count: int = 0
    while count < len(answer):
        if contains_char(answer, guess[count]) is True:
            if guess[count] == answer[count]:
                display += GREEN_BOX
            else:
                display += YELLOW_BOX
        else:
            display += WHITE_BOX
        count += 1
    return display


def input_guess(n: int) -> str:
    """Makes sure the word has a valid length."""
    guess: str = input(f"Enter a {n} character word:")
    while len(guess) != n:
        guess = input(f"That wasn't {n} chars! Try again:")
    return guess


if __name__ == "__main__":
    main(secret="codes")
