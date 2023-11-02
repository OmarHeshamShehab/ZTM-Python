import sys
from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("you are a genius!")
            return True
    else:
        print("hey bozo, I said 1~10")
        return False


answer = randint(1, 10)
print(answer)
if __name__ == "__main__":
    while True:
        try:
            guess = int(input(f"Please enter your guess in a range between 1~10 : "))
            if run_guess(guess, answer):
                break

        except ValueError as err:
            print(err)
