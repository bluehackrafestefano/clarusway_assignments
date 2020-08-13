# users database - a particular index corresponds to a specific user
names = ["James", "John", "Emma"]
surnames = ["Oliver", "Smith", "Brown"]
birth_days = [15, 22, 8]
birth_months = [3, 6, 12]
birth_years = [1984, 1994, 2001]

a=list(zip(birth_days, birth_months, birth_years))  # Three lists of birth records into list of tupples
print(a)

while True:
    name=input("Please enter your name: ")
    for i in range(len(names)-1):
        if name==names[i]:
            print("You are a customer!")
            break
        else:
            print("You are not a customer!")
        break

while True:
    surname=input("Please enter your surname: ")
    for i in range(len(names)-1):
        if surname==surnames[i]:
            print("You are a customer!")
            break
        else:
            print("You are not a customer!")
        break

while True:
    birthday=input("Please enter your birthday (MM/DD/YYYY): ")
    
    b=birthday.split("/")  # This will make input birthdate a list of string numbers
    print(b)
    brth=tuple([int(i) for i in b])  # Converting birth dates to int
    print(brth)
    
    for i in range(len(names)-1):
        if brth==a[i]:
            print("You are a customer!")
            break
        else:
            print("You are not a customer!")
        break