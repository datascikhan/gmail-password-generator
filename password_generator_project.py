"""
🔑 Password Generator Python Project 

📌 Project kya karega?
Password Generator ek aisa Python project hai jo strong, random aur secure passwords 
generate karega.

Iska main kaam:
Random passwords banana
User se input lena (length, characters type)
Strong password generate karna (uppercase, lowercase, numbers, symbols)
Optional: password ko file mein save karna

🧠 Is project mein hum kya kya use karenge?

1. 🔤 Python Basics
Variables
Loops (for, while)
Conditions (if-else)
Functions


2. 🎲 Random Module
Python ka built-in module:

random.choice() → random character pick karega
random.shuffle() → password ko mix karega


3. 🔡 String Module
string.ascii_lowercase → abc...
string.ascii_uppercase → ABC...
string.digits → 123...
string.punctuation → !@#$...



4. 📥 User Input
input() use hoga user se data lene ke liye
password length
kya numbers chahiye?
kya symbols chahiye?


5. 📁 File Handling (Advanced)
Password ko file mein save karna (.txt file)

🎯 Project Flow (Simple samajh lo)
User se poochho:
password length
kya uppercase chahiye
kya numbers chahiye
kya symbols chahiye
Character pool create karo
Random password generate karo
Password display karo
Optional: file mein save karo

🔐 Password Strength Checker – Explanation

📌 Yeh feature kya karega?
Yeh check karega ke generated ya user ka password:
Weak hai 😐
Medium hai 🙂
Strong hai 💪

🧠 Strength kaise check hoti hai?
Hum kuch rules use karenge:

✅ 1. Length
< 6 → Weak
6-10 → Medium
10 → Strong

✅ 2. Character Types
Check karenge ke password mein kya kya hai:

Lowercase (a-z)
Uppercase (A-Z)
Numbers (0-9)
Symbols (!@# etc)

""" 
import random
import string

# password generator function
def generate_password(lenght, use_upper, use_numbers, use_symbols):

    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    
    if use_numbers:
        characters += string.digits
        
    if use_symbols:
        characters += string.punctuation
    
    password = []

    for i in range(lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    return ''.join(password)

# Password Strength checker
def check_strength(password):

    score = 0

    # Lenght Check
    if len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score +=1

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1

    # Number check
    if any(char.isdigit() for char in password):
        score += 1

    # Symbols check
    if any(char in  string.punctuation for char in password):
        score += 1
    
    # Result decide karna
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
    

# =========================
# MAIN PROGRAM
# =========================
print("Advance Password Generator + Strength Checker")

while True:

    print("\n 1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Option choose karo: ")

    # Generate Password
    if choice == '1':

        length = int(input("Password length: "))

        upper = input("Uppercase chahiye? (yes/no): ").lower() == 'yes'
        numbers = input("Numbers chahiye? (yes/no): ").lower() == 'yes'
        symbols = input("Symbols chahiye? (yes/no): ").lower() == 'yes'

        password = generate_password(length, upper, numbers, symbols)
        print("\n✅ Generate Password:", password)

        # Strength check bhi yahin kar denge
        strength = check_strength(password)
        print("Strength:", strength)

        # save option
        save = input("Save karna hai? (yes/no): ").lower()

        if save == 'yes':
            with open("password.txt", "a") as file:
                file.write(password + " | " + strength + "\n")
            print("Saved successfully")

        
    elif choice == '2':

        user_pass = input("Apna password enter karo: ")
        strength = check_strength(user_pass)
        print("Strength:", strength)

    # Exit
    elif choice == '3':
        print("Program band ho raha hai.")
        break
    else:
        print("Invalid option, dobara try karo.")




