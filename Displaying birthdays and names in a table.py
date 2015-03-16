#Harry Robinson
#27/02/2015
#printing the file created as a table

import pickle
class Person:
    def __init__(self):
        self.name = None
        self.dob = None
with open("names.dat", mode= "rb") as binary_file:
    people = pickle.load(binary_file)
print("| {0} | {1} |".format("-"*15))
print("| {0} | {1} |".format(
