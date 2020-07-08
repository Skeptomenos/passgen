#!/usr/bin/python
import getparameter
import generator

passwort = ""
while len(passwort) < int(getparameter.pwlength):
    passwort += generator.create_random_character()

print("Dein Passwort ist: " + str(passwort))

#passwort = ''.join(generator.create_random_character() while len(passwort) < range(int(getparameter.pwlength)))

#print("Dein Passwort soll aus " + str(pwLength) + " Zeichen bestehen")
#if pwNumber == True:
#    print ("Dein Passwort soll Zahlen enthalten")
#else:
#    print("Dein Passwort soll keine Zahlen enthalten.")

#if pwSpecial == True:
#    print("Dein Passwort soll Zeichen enthalten.")
#else:
#    print("Dein Passwort soll keine Zeichen enthalten.")

