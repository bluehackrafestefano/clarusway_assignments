word = input("Please enter a sentence: ")

new_dic ={}
for char in word:
    new_dic [char] = word.count(char)
print(new_dic)