rafe_python_assignment_8

year= int(input("Please enter a name to check if it's leap year or not: "))

if (year%400==0) or (year%100!=0) and (year%4==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")