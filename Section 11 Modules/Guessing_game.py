import sys
from random import randint

first_number = sys.argv[1]
second_number = sys.argv[2]


created_number = randint(int(first_number), int(second_number))
print(created_number)


while True:
    try:
        user_guess = input(
            f"Please enter your guess in a range between {first_number} & {second_number} : "
        )
        if int(first_number) <= int(user_guess) and int(user_guess) <= int(
            second_number
        ):
            if int(user_guess) == created_number:
                print("you won guess")
                break
        else:
            print("out of range dude")

    except ValueError as err:
        print(err)
