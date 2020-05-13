#!/bin/bash

clear
# read -p "Please write your name: " name

# echo "Hello $name"

# if (( name == Faruk ))
# then
#     echo "I know you"
# fi

# cat << END
# This 
# prints
# every
# line
# END

my_fizzbuzz_code=$ (cat << END
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    
    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("buzz")
    
    else:
        print (i)
END)
echo my_fizzbuzz_code