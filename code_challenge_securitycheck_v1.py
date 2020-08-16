names = ["James", "John", "Emma"]
surnames = ["Oliver", "Smith", "Brown"]
birth_months = [3, 6, 12]
birth_days = [15, 22, 8]
birth_years = [1984, 1994, 2001]
while True:
    name = input("Please enter your name:").lower()
    if name == "q":
        break
    names_list = list(map(lambda x: x.lower(), names))
    # print(names_list)
    if name not in names_list:
        print("You are not a customer!")
        continue
    else:
        name_index = names_list.index(name)
        # index(name) listeye bakıyor ve eşleşen ilk ifadeyi sorguluyor
        surname = input("Please enter your surname:").lower()
        # print(name_index)
    if surname != surnames[name_index].lower():
        print("You are not a customer!")
        continue
    else:
        birth_date = input("Please enter your birthday (MM/DD/YYYY):").lower()
        split_birth_date = birth_date.split('/')
        # print(split_birth_date)
        if int(split_birth_date[0]) == birth_months[name_index] and int(split_birth_date[1]) == birth_days[name_index] and int(split_birth_date[2]) == birth_years[name_index]:
            print("You are a customer!")
            print(f'{name} {surname}' " welcome!")
            break
        else:
            print("You have entered an incorrect value!")
            continue