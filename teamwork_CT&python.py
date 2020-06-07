list=[1,2,3,4,5,6,7,8,9,0]

# print(len(list))

s = int(input("Please write starting index: "))
while 


if s < 0 or s > (len(list)-1):
    print("Out of range!")
    
else:
    print(list[s])

e = int(input("Please write ending index: "))

if e < 1 or e > len(list):
    print("Out of range!")
else:
    print(list[e])

#CT concepts: Decomposition (first take input, than check them if they are valid or not, finally slice values and print)
# Patern Recognition (find the way of checking value for the starting point, apply it for the end point)
# Algorithm design is the code itself :)
# Abstraction (the list is not important, the output messages not important)