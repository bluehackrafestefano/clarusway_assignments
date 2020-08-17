names = ["James", "John", "James", "James"]
surnames = ["Oliver", "Smith", "Brown", "Last"]
birth_months = [3, 6, 12, 1]
birth_days = [15, 22, 8, 1]
birth_years = [1984, 1994, 2001, 2002]

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

while True:
    name = input("Please enter your name\n(Press 'q' to exit!) : ")
    a=list_duplicates_of(names, name)
    # print(a)

    if name == "q":
        break

    if a == []:
        print("You are not a customer")
        continue
    else:
        surname = input("Please enter your surname:")
        res_list = [surnames[i] for i in a]
        # print(res_list)
        if surname not in res_list:
            print("You are not a customer")
            continue
        else:
            # print(surnames.index(surname))
            p=surnames.index(surname)
            birth_date = input("Please enter your birthday (MM/DD/YYYY):")
            split_birth_date = birth_date.split('/')
            print(split_birth_date)
            if int(split_birth_date[0]) == birth_months[p] and int(split_birth_date[1]) == birth_days[p] and int(split_birth_date[2]) == birth_years[p]:
                print("You are a customer!")
                print(f'{name} {surname}' " welcome!")
                break
            else:
                print("You have entered an incorrect value!")
                continue