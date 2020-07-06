# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# CT decomposition: Break down the problem into 1) get input 5 times to a list 2) sort numbers 3) get last and largest one
# CT algorithm design: This py code itself
# CT abstraction: Assume user enter numbers everytime, its not important the size of the number entered

numbers=[]
count=1
while count < 6:
    numbers.append(int(input(f"Please enter number {count}: ")))
    count+=1
new_numbers= sorted(numbers)
max_number=new_numbers[-1]
print(f"Maximum number you entered is : {max_number}")

