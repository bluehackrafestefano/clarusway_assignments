people = []                                     # Declare new variable "people" and set to an empty list
​
isRunning = True                                # Declare new variable "isRunning" and set it to True
​
while isRunning:                                # Loops when "isRunning" is True
​
    print("\n" * 50)                            # Prints 50 new lines clearing the console
    print("================")
    print("1: Add Person")
    print("2: Delete Person")                   # Print Menu
    print("3: List People")
    print("4: Quit")
    print("================")
    print("\n")                                 # Print Blank Line
​
    sel = input("Pick One: ")                   # Set "sel" to the output of input()
​
    if sel == "1":                              # Runs if user entered "1"
​
        person = []                             # Declare new variable "person" and set to an empty list
        print("\n" * 50)                        # Prints 50 new lines clearing the console
​
        name = input("Name: ")                  # Gets person's name and passes it to "name"
        person.append(name)                     # Append person's name to "person"
​
        age = input("Age: ")                    # Gets person's age and passes it to "age"
        person.append(age)                      # Append person's age to "person"
​
        address = input("Address: ")            # Gets person's address and passes it to "address"
        person.append(address)                  # Append person's address to "person"
​
        phoneNumber = input("Phone Number: ")   # Gets person's phone number and passes it to "phoneNumber"
        person.append(phoneNumber)              # Append person's phone number to "person"
​
        people.append(person)                   # Appends "person" to "people"
​
    elif sel == "2":                            # Runs if user entered "2"
​
        print("\n" * 50)                        # Prints 50 new lines clearing the console
​
        count = 1                               # Declare new variable "count" and set to 1
​
        for x in people:                        # Runs for every person
            print(str(count) + ": " + x[0])     # Prints "count" and person's name
            count += 1                          # Increments "count" by 1
​
        deleted = int(input("Pick One: ")) - 1  # Gets user to be deleted and converts it to an integer
​
        if deleted == len(people):              # Runs if number entered is valid
​
            del(people[deleted])                # Deletes the selected user
​
    elif sel == "3":                            # Runs if user entered "3"
​
        print("\n" * 50)                        # Prints 50 new lines clearing the console
​
        for x in people:                        # Runs for every person
​
            print("Name: " + x[0])              # Prints person's name
            print("Age: " + x[1])               # Prints person's age
            print("Address: " + x[2])           # Prints person's address
            print("Phone Number: " + x[3])      # Prints person's phone number
​
            print("\n")                         # Prints a blank line
​
        input("Press enter/return to continue") # Waits for the user to press enter/return
​
    elif sel == "4":                            # Runs if user entered "4"
        isRunning = False                       # Sets "isRunning" to False
Collapse