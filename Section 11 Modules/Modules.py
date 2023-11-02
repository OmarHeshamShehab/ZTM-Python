import datetime
from collections import Counter, defaultdict

li = ["a", "b", "c", "d", "f", "a", "a", "j", "j", "n", "n", "n", "V", "v", "x"]
print(Counter(li))

dictionary = {"a": 1, "b": 2}
default_dictionary = defaultdict(lambda: 5, {"a": 1, "b": 2})

print(dictionary["a"])
print(default_dictionary["c"])

print(datetime.date.today())
