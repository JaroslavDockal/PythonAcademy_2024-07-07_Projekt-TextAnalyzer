"""
TextAnalyzer.py: první projekt do Engeto Online Python Akademie

author: Jaroslav Dočkal

email: jaroslav.dockal@outlook.com

discord: jaroslav.dockal
"""

import hashlib
import re

DEBUG = True

def debug_print(message):
    if DEBUG:
        print(f"Debug: {message}")

users = {
    'bob': '202cb962ac59075b964b07152d234b70',
    'ann': '482c811da5d5b4bc6d497ffa98491e38',
    'mike': '482c811da5d5b4bc6d497ffa98491e38',
    'liz': '482c811da5d5b4bc6d497ffa98491e38'
}

def hash_password(password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    debug_print(f"hashed password is {hashed}")
    return hashed

def authenticate(username, password):
    if username in users:
        debug_print(f"found user {username}")
        if users[username] == hash_password(password):
            debug_print("password matches")
            return True
        else:
            debug_print("password does not match")
    else:
        debug_print("user not found")
    return False

def select_text():
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
    try:
        choice = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
        if choice in range(len(TEXTS)):
            return TEXTS[choice]
        else:
            print("Invalid choice. Terminating the program...")
            exit()
    except ValueError:
        print("Invalid input. Terminating the program...")
        exit()

TEXTS = [
    """Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive topographic feature that rises 
    sharply some 1000 feet above Twin Creek Valley to an elevation of more 
    than 7500 feet above sea level. The butte is located just north of US 
    30N and the Union Pacific Railroad, which traverse the valley.""",

    """At the base of Fossil Butte are the bright red, purple, yellow and 
    gray beds of the Wasatch Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor and steepen abruptly. 
    Overlying them and extending to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, which are about 300 feet 
    thick.""",

    """The monument contains 8198 acres and protects a portion of the largest 
    deposit of freshwater fish fossils in the world. The richest fossil 
    fish deposits are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils represent several 
    varieties of perch, as well as other freshwater genera and herring 
    similar to those in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present."""
]

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper())
    lowercase_count = sum(1 for word in words if word.islower())
    numeric_strings = [int(word) for word in words if word.isdigit()]
    numeric_count = len(numeric_strings)
    numeric_sum = sum(numeric_strings)

    print("----------------------------------------")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")
    print("----------------------------------------")

    length_freq = {}
    for word in words:
        length = len(word)
        if length not in length_freq:
            length_freq[length] = 0
        length_freq[length] += 1

    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    for length in sorted(length_freq):
        print(f"{length:>3}| {'*' * length_freq[length]:<12} |{length_freq[length]}")

def main():
    username = input("username: ")
    #TODO Jak skrýt heslo na vstupu?
    password = input("password: ")

    if authenticate(username, password):
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        text = select_text()
        analyze_text(text)
    else:
        print("Unregistered user, terminating the program...")

if __name__ == "__main__":
    main()
