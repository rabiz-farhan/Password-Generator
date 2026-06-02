import random
import string

#function 1 for character pool
def character_pool(use_upper,use_lower,use_digit,use_special):
    characters = ""

    if use_upper == "yes":
        characters += string.ascii_uppercase

    if use_lower == "yes":
        characters += string.ascii_lowercase

    if use_digit == "yes":
        characters += string.digits

    if use_special == "yes":
        characters += string.punctuation
    return characters
#function 2 for random password 
def generate_password(length,characters,use_upper,use_lower,use_digit,use_special):
    password = []
    #force adding atleast one character type
    if use_upper == "yes":
        password.append(random.choice(string.ascii_uppercase))

    if use_lower == "yes":
        password.append(random.choice(string.ascii_lowercase))

    if use_digit == "yes":
        password.append(random.choice(string.digits))

    if use_special == "yes":
        password.append(random.choice(string.punctuation))

    #filling remaining length randomly
    remaining_length= length - len(password)

    for i in range(remaining_length):
        password.append(random.choice(characters))
    #shuffling password so forced characters are not predictable
    random.shuffle(password)

    #converting list into string
    password= "".join(password)
    
    return password


#-----Main program-----#

#User input
length= int(input("Enter the password length: " ))
use_upper= input("Should the password contain uppercase letters?(YES/NO): ")
use_lower= input("Should the password contain lowercase letters?(YES/NO): ")
use_digit= input("Should the password contain numbers?(YES/NO): ")
use_special= input("Should the password contain special characters?(YES/NO): ")

#Making character pool
characters= character_pool(use_upper,use_lower,use_digit,use_special)

#Variable for comparing with password length
selected_types = 0

if use_upper == "yes":
    selected_types +=1

if use_lower == "yes":
    selected_types +=1

if use_digit == "yes":
    selected_types +=1

if use_special == "yes":
    selected_types +=1


#Ensuring the character pool isn't empty
if characters == "":
    print("Error: You must select atleast one character type.")
#validating password length
elif length < selected_types:
    print("Error: password length is too short for selected character types")
else:
#Generating a random password from the character pool
    password= generate_password(length,characters,use_upper,use_lower,use_digit,use_special)

    print("\nGenerated Password:", password)
