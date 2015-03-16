#Harry Robinson
#02/03/2015
#Reading in a file and displaying as a table

import pickle
class Person:
    def __init__(self):
        self.name = None
        self.dob = None
with open("names.dat", mode = "rb") as binary_file:
    people = pickle.load(binary_file)
    print("|Name|Dob|")
    for aPerson in people:
        print("{0}{1}{2}".format("|", "-"*10,"|"))
        print("|{0:<4}|{1:<5}|".format(aPerson.name, aPerson.dob))
