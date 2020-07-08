#!/usr/bin/python
from src import getparameter
import random
#import string

# wählt einen zufälligen kleinen Buchstaben
def get_random_letter():
    letters = "abcdefghijklmnopqrstuvwxy"
    result_letter = random.choice(letters)
    #print("get_random_letter " + result_letter)
    return result_letter

# wählt eine zufällige Zahl von 0 bis 9
def get_random_number():
    numbers = "0123456789"
    result_numbers = random.choice(numbers)
    #print("get_random_number: " + result_numbers)
    return result_numbers

# wählt ein zufälliges Satzzeichen
def get_random_special():
    special = "!§$%&/()=?*+-_@<>"
    result_special = random.choice(special)
    #print("get_random_special: " + result_special)
    return result_special

## ermitteln Typen des Passowrts anhand der enthaltenden Zeichen
def get_password_type():
    if getparameter.boolspecial == True and getparameter.boolnumber == True:
        pwtype = 1
    elif getparameter.boolspecial == False and getparameter.boolnumber == True:
        pwtype = 2
    elif getparameter.boolspecial == True and getparameter.boolnumber == False:
        pwtype = 3
    else:
        pwtype = 4
    return pwtype

# generiert eine Zeichen für das Passwort, je nachdem welche Zeichentypen enthalten sind
def create_random_character():
    a = random.randint(0, 999)
    pwtype = get_password_type()
    if pwtype == 1: ## Sonderzeichen und Nummern enthalten
        if a <= 333:
            result = str(get_random_letter())
            #print("create_random_character: " + result)
            return result
        elif a > 333 and a < 666:
            result = str(get_random_number())
            #print("create_random_character: " + result)
            return result
        elif a > 666:
            result = str(get_random_special())
            #print("create_random_character: " + result)
            return result
    elif pwtype == 2: ## Zahlen, Keine Sonderzeichen
        if a < 500:
            result = str(get_random_letter())
            #print("create_random_character: " + result)
            return result
        else:
            result = str(get_random_number())
            #print("create_random_character: " + result)
            return result
    elif pwtype == 3: # Sonderzeichen, keine Zahlen
        if a < 500:
            result = str(get_random_letter())
            #print("create_random_character: " + result)
            return result
        else: #nur Buchstaben
            result = str(get_random_special())
            #print("create_random_character: " + result)
            return result
    else:
        result = str(get_random_letter())
        #print("create_random_character: " + result)
        return result


# def get_random_string(length):
#    letters = string.ascii_lowercase
#    result_str = ''.join(random.choice(letters) for i in range(length))
#    print("Random string of length", length, "is:", result_str)
