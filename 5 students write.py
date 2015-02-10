#Harry Robinso
#10-02-2015
#reading in 5 lines to a file

with open("5students.txt", mode = "w", encoding = "utf-8") as my_file:
    for count in range(5):
        name = input("Enter the name: ")
        my_file.write(name + "\n")
