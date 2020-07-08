#!/usr/bin/python

# Nutzereingabe, wie lang das Passwort sein soll
def get_password_length():
    pwLength = int(input("Wie lange soll dein Passwort sein sein? "))
    if pwLength < 6:
        print("Das Passwort muss mindestens 6 Zeichen lang sein. Bitte versuche es erneut.")
        get_password_length()
    return int(pwLength)


## Nutzereingabe, ob das Passwort Zahlen enthalten soll
def ask_numbers():
    answer = (input("Soll das Passwort Zahlen enthalten? [J/n] ")).upper()
    if answer == "Y" or answer == "J":
        b = True
    elif answer == "N":
        b = False
    else:
        print("Ich habe deine Antwort nicht verstanden. Bitte versuche es noch ein mal.\n")
        finish()
    return b


## Nutzereingabe, ob das Passwort Sonderzeichen enthalten soll
def ask_special():
    answer = (input("Soll das Passwort Sonderzeichen enthalten? [J/n] ")).upper()
    if answer == "Y" or answer == "J":
        b = True
    elif answer == "N":
        b = False
    else:
        print("Ich habe deine Antwort nicht verstanden. Bitte versuche es noch ein mal.\n")
        finish()
    return b

pwlength = get_password_length()
boolnumber = ask_numbers()
boolspecial = ask_special()