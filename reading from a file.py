#Harry Robinson
#10-02-2015
#Reading data from a file

with open("5students.txt", mode = "r", encoding = "utf-8")as my_file:
    for line in my_file:
        print(line, end="")
