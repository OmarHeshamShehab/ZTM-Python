myfile = open("Section 13 I_O File/test.txt")
print(myfile.read())
print("---------------------------")
myfile.seek(0)  # seek is used to move cursor to next line
print(myfile.readline())  # reads only first line
print("---------------------------")
print(myfile.readlines())  # list to read all the lines
myfile.close()  # close the file
print("---------------------------")
# no need to close, it is done automaticly
# mode by defualt is r if we want to write mode = 'w' and 'w' deletes all text and starts again from begining
# mode write mode = 'w'  creates new fileif it does't exists
# mode = r+ read and write to file adds the data from begining and don't delete any previous data
# mode = a append text to last place in file
with open("./Section 13 I_O File/test.txt", mode="w") as my_file:
    text = my_file.write(" omar")
    print(text)
