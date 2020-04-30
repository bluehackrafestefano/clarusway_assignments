num = input("This program gives you the prime numbers between 1 to your entered limit number\nPlease enter a positive integer number: ")

while not num.isdigit():
  print ("Do not use any entries other than numeric values")
  num = input ("Please enter a positive integer number: ")

while int(num) < 1:
  print ("Not a positive number")
  num = input ("Please enter a positive integer number: ")

a = int(num)
prime = []

if a < 11:
    if a < 2:
        prime = []
    elif a < 3:
        prime = [2]
    elif a < 5:
        prime = [2, 3]
    elif a < 7:
        prime = [2, 3, 5]
    else:
        prime = [2, 3, 5, 7]

else:
    prime = [2, 3, 5, 7, 11]
    for i in range (11, a):
        if ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) and (i != 11)):
            prime.append(i)

print(f"Prime numbers between 1 and {a} are:\n{prime}")