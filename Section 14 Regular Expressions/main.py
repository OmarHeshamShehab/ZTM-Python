import re

"""
it is a case senstive
"""
pattern = re.compile(
    "search inside of this text please and let me know if this is repeated!"
)
pattern2 = re.compile(r"[a-zA-Z].([a])")
pattern3 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern4 = re.compile(r"^(?=.*[&@$%])[A-Za-z\d&@$%]{7,}[0-9]$")
string = "search inside of this text please"
email_validation = "omar.hesham.shehab@gmail.com"
pass_validation = "hdjkahskdha5534%$9l"
a = re.search("this", string)

print(a.span())  # start and end of the index in the sentence
print(a.start())
print(a.end())

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)  # needs to be a full match
d = pattern.match(string)  # check whether pattern exsists in string or not
e = pattern3.search(email_validation)
f = pattern4.fullmatch(pass_validation)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)  # as it doesn't end with number
