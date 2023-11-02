while True:
    try:
        input_value = int(input("enter a number : "))
        10 / input_value
    except ValueError as e:
        print(f"please enter a number!!! this is {e}")
    except ZeroDivisionError as e:
        print(f"can't be divided by {e}")
    else:
        print("thank you!")
        break


def division(n1, n2):
    try:
        return n1 / n2
    except (ZeroDivisionError, TypeError) as err:
        print(err)


print(division(1, 0))
