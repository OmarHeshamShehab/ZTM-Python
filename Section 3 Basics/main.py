"""
 test
"""
# birth_year = input("what year were you born? : ")
# age = 2023 - int(birth_year)
# print(f" you are now {age} years old")
#
# username = input("enter user name: ")
# password = input("enter the password: ")
# length = len(password)
#
# print(f" hi {username}, your password {length * '*'} is {length} letters length")

# dictionary = {
#     'a': 1,
#     'b': 2
# }
#
# print(dictionary['b'])

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# addition = 0
# for i in my_list:
#     addition += i
# print(addition)
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
# ]
#
# for row in picture:
#     for pixel in row:
#         if pixel == 0:
#             print(" ", end='')
#         else:
#             print("*", end='')
#     print('')

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []

# for char in some_list:
#     if some_list.count(char) > 1:
#         if char not in duplicates:
#             duplicates.append(char)

# print(duplicates)

even = []


def highest_even(li):
    """
    getts high even number
    """
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)


print(highest_even([10, 2, 3, 4, 8, 11, 20]))
