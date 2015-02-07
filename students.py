#Harry Robinson
#06/02/2015
#Student file

with open("students.txt", mode = "a", encoding= "utf-8") as my_file:    
    for count in range(3):
        name = input("Enter the name: ")
        my_file.write(name + "\n")
with open("students.txt", mode = "r", encoding= "utf-8") as my_file:
    index = 1
    for line in my_file:
        print(index, line)
        index = index + 1

