from turtle import *
import random

# vérifie si la lettre est valide
def estLettreValide(lettre):    
    if lettre not in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):            
        return False
    return True

# vérifie si le mot est valide
def estMotValide(mot):
    for lettre in mot:
        if not estLettreValide(lettre):
            return False
    return True

def afficheElementPendu(nbErreurs):    
    match nbErreurs:
        case 1:
            forward(120)            
        case 2:
            backward(60)
            left(90)
            forward(70)
        case 3:
            forward(70)
        case 4:
            forward(70)
        case 5:
            right(90)
            forward(80)
        case 6:
            right(90)
            forward(30)
        case 7:
            right(90)
            forward(1)
            circle(10)

# Ouvrir le fichier en lecture seule
file = open('dico.txt', "r")
lines = file.readlines()

# Choisir un mot valide dans le dictionnaire
while True:    
    mot = random.choice(lines).strip().lower() 
    if estMotValide(mot):
        break
#print(mot)
tabLettresReponse = []
for lettre in mot:
    tabLettresReponse.append('-')
nbErreurs = 0
nbEssaisPourTest = 0
limiteNbEssaisPourTest = 15

#boucle
while True and nbEssaisPourTest < limiteNbEssaisPourTest:
    nbEssaisPourTest += 1
    lettre = input("Saisir une lettre sans accent : ")
    if not estLettreValide(lettre):
        print("Cette lettre n'est pas valide")
        continue
    if lettre not in mot:
        nbErreurs += 1
        afficheElementPendu(nbErreurs)
        #print(nbErreurs)
        if nbErreurs < 7:
            continue            
        else:
            print(f'Partie perdue, le mot à trouver était : {mot}')
            break
    else:
        #on affiche la lettre aux emplacements où elle se trouve dans le mot à chercher
        for i in range(len(mot)):
            if mot[i] == lettre:
                tabLettresReponse[i] = lettre
        motReponse = ''.join(tabLettresReponse)
        print(motReponse)
        if motReponse == mot:
            print('Partie gagnée !')
            break