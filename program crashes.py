#Harry Robinson
#6/02/2015
#Program crashes

valid = False
while not valid: 
    try:
        number = int(input("Enter a number: "))
        print(number)
    except ValueError:
        print("Value entered was not a number")
    valid = True
