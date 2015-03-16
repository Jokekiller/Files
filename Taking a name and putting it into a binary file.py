#Harry Robinson
#10-02-2015
#Class and binary files

import pickle

class Person:
    def __init__(self):
        self.name = None
        self.dob = None
people = []
#self = Person()
for count in range(2):
    aPerson = Person()
    aPerson.name = input("Enter the name: ")
    aPerson.dob = input("Enter their date of birth (YYYY-MM-DD): ")
    people.append(aPerson)

with open("names.dat", mode = "wb") as binary_file:
    pickle.dump(people, binary_file)

with open("names.dat", mode= "rb") as binary_file:
    people = pickle.load(binary_file)
<<<<<<< HEAD
=======
    print("|Name|Dob|")
    for aPerson in people:
        print("|{0:<10}|{1:<10}".format(aPerson.name, aPerson.dob))
>>>>>>> branch 'master' of https://github.com/Jokekiller/Files.git

