#Harry Robinson
#10-02-2015
#Class and binary files

import pickle

class Person:
    def __init__(self):
        self.name = None
        self.dob = None
people = []
self = Person()
for count in range(2):
    Person.name = input("Enter the name: ")
    Person.dob = input("Enter their date of birth (YYYY-MM-DD): ")
    people.append(Person)

with open("names.dat", mode = "wb") as binary_file:
    pickle.dump(people, binary_file)

with open("names.dat", mode= "rb") as binary_file:
    people = pickle.load(binary_file)

