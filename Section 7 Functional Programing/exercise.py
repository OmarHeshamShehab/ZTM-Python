from functools import reduce

animals = ["dog", "cat", "bird"]


# 1 Capitalize all of the pet names and print the list
def capitallize(item):
    return item.upper()


my_pets = ["sisi", "bibi", "titi", "carla"]
pets = map(capitallize, my_pets)

print(*pets)
# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, my_numbers)))


# 3 Filter the scores that pass over 50%
def over50(item):
    return item > 50


scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(over50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate(acc, item):
    print(acc + item)
    return acc + item


print(reduce(accumulate, my_numbers, (reduce(accumulate, scores, 0))))

mylist = [5, 4, 3]

print(list(map(lambda item: item**2, mylist)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

some_list2 = ["a", "b", "c", "b", "d", "m", "n", "n"]

non_repeated = list[{char for char in some_list2 if some_list2.count(char) > 1}]

print(non_repeated)
