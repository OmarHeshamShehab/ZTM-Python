"""
map,filter,zip & reduce example
"""


from functools import reduce

new_list = [2, 4, 6, 8, 9]
new_list2 = [20, 40, 60, 80, 9]
new_list3 = [-4, -6, -8, -99, -123]


def multiplyby2(item):
    return item * 2


def is_odd(item):
    return item % 2 != 0


##print(list(map(multiplyby2, new_list)))
print(list(map(lambda item: item * 2, new_list)))
##print(list(filter(is_odd, new_list)))
print(list(filter(lambda item: item % 2 != 0, new_list)))
##print(list(zip(new_list, new_list2, new_list3)))

"""
what will happen below is that reduce method takes 3 parameters:
1 = function itself
2 = the data that will be used list for example
3 =  the initial value that will start with in this case it will be the acc 
"""


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(reduce(accumulator, new_list, 0.1))
print(reduce(lambda acc, item: acc + item, new_list))

# list of comprehension works on list[],set{}, dictionary

comp_list = []

for i in "hellooooo":
    comp_list.append(i)
print(comp_list)

cpmprehension_list = [char for char in "hellooooo"]
print(cpmprehension_list)

number_range = [num for num in range(0, 100)]
print(number_range)

number_range2 = [num**2 for num in range(0, 100)]
print(number_range2)

number_range2 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(number_range2)

simple_dict = {"a": 1, "b": 2, "c": 3}

my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}

print(my_dict)

list_to_dict = [1, 2, 3, 4, 5]
my_dict2 = {n1: n1**2 for n1 in list_to_dict}

print(my_dict2)
