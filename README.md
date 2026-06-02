# Password-Generator
A Python project that generates secure customizable passwords using randomization and validation logic.
# Features
Generates random secure passwords

Allows users to choose password length

Supports upper case and lower case letters, numbers and special characters to be included in the password

Guarantees that the selected character types are included in the final password at least once

Randomly shuffles password characters for improved unpredictability

Prevents password generation if no character type is selected

Validates whether password length is sufficient for selected character types
# Methods and Concepts used
Functions:

The project uses separate functions to improve code organization,efficiency and reuseability, exps:
character_pool()- builds a character set that contains all the character types selected by the user.
generate_password()- creates the final password through the character set.

Randomization:

The random module is used to randomly select characters and shuffle the password for unpredictability.

String Module:

The string module provides predefined character sets such as uppercase letters,lowercase letters,digits,punctuation symbols

Lists and String Manipulation:

Lists are used to temporarily store password characters before converting them into the final password string using "".join()

Conditional Logic and loop:

if statements are used to check user preferences,validate input,ensure required character types are included.
count controlled loop is used to iterate through the entire password length selected by the user and concatenate the characters from character pool to generate the password.

Input Validation:

The program checks whether at least one character type is selected, and whether the password length is sufficient for the selected character types.
# Development process
This project was developed through three stages of programming:

1.Basic password generator(raw version)

2.Function-based version

3.Completed version with validation checks and guaranteed character inclusion 

note: The earlier two development versions are stored in the old_version folder.
# What I learned
Through this project i learned to understand and handle import modules.

Do modular programming using functions.

Generate a random password through random module and count control loop.

Input validation and error handling with debugging and refining program logic.

List manipulation and converting list to string.

Improving program structure through iterative development and thinking for possible errors in the output.
# Example Output
Scenario 1: successful output of password

Enter the password length: 10 

Should the password contain uppercase letters? yes

Should the password contain lowercase letters? yes

Should the password contain numbers? yes

Should the password contain special characters? yes

Generated Password: A7!kdP2@Lm

Scenario 2: No character type selected

Enter the password length: 4

Should the password contain uppercase letters? no

Should the password contain lowercase letters? no

Should the password contain numbers? no

Should the password contain special characters? no

Error: You must select at least one character type.

Scenario 3: password length too short

Enter the password length: 2

Should the password contain uppercase letters? no

Should the password contain lowercase letters? yes

Should the password contain numbers? yes

Should the password contain special characters? yes

Error: Password length is too short for selected character types.


