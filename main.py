# Zak Alexandre Kiraly
# 12 sept 2023
# TP2

import random

recommencer = True

#boucle qui permet a l'utilisateur de recommencer le jeu
while(recommencer == True):
    chiffre_aleatoire = random.randint(1, 1000)
    print(chiffre_aleatoire)
    reponse = False

    #boucle qui permet a l'utilisateur de
    while reponse == False:
        guessed_number = int(input("quel est ton essait (nombre)? \n"))

        if guessed_number < chiffre_aleatoire :
            print("trop petit!")

        if guessed_number > chiffre_aleatoire :
            print("trop grand!")

        if guessed_number == chiffre_aleatoire :
            print("oui, c'est ca!")
            reponse = True

    choix_rec = str(input('veux-tu recommencer? o/n \n'))
    if choix_rec == 'o':
        recommencer = True
    else:
        recommencer = False