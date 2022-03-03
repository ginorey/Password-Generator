import random

# user input 
length = int(input("How long do you want it to be? "))
characters = input("What characters would you like to include? ")

# converting characters input into list
char = list(characters)

# removing white spaces if user inputted them
for i in char:
    if char.__contains__(" "):
        char.remove(" ")
    else: 
        continue 

# randomly choosing from char list
temp = random.choices(char, k=length)
# joining from list to string
temp2 = "".join(temp)                        


password = "Your generated password is: {}".format(temp2)
print(password)
    