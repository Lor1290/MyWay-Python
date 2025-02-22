#Import
import random
import string

cicle_1 = True
cicle_2 = True

#Introduction
print()
print("Welcome to the app were you build your own random password")
print("Now...")

#DigitNumber
while cicle_1:

    cicle_1 = True
    cicle_2 = True

    print()

    try:
        password = int(input(">>> Digit the number of password do you need: "))
    except ValueError:
        print("Invalid data, retry")
        continue

    try:
        lenght = int(input(">>> Select the lenght for the password: "))
    except ValueError:
        print("Invalid data, retry")
        continue

    print()
    #Resault
    for x in range(password):
        print("> " + "".join(random.choice(string.ascii_letters + string.digits) for i in range(lenght)))
    print()

    #Cicle Y/N
    while cicle_2:

        decision = input(("Want to continue? (y/n) "))

        if decision.lower() == "y":
            cicle_2 = False

        elif decision.lower() == "n":
            cicle_2 = False
            cicle_1 = False

        else:
            print("Invalid data, retry")
            
