import string
from turtle import *
import random


def est_lettre_valide(lettre):
    if lettre in string.ascii_lowercase:
        return True
    return False


def est_mot_valide(mot):
    for lettre in mot:
        if not est_lettre_valide(lettre):
            return False
    return True


def affiche_element_pendu(nb_erreurs):
    match nb_erreurs:
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
            forward(0.1)
            circle(10)
            up()
            sety(ycor() - 20)
            left(90)
            down()
            # haut du tronc
            forward(10)
            # bras droit
            left(90)
            forward(20)
            # bras gauche
            up()
            right(180)
            setx(xcor() - 20)
            down()
            forward(20)
            # bas du tronc
            up()
            left(90)
            setx(xcor() + 20)
            down()
            forward(25)
            x, y = pos()
            # jambe gauche
            right(30)
            forward(30)
            # jambe droite
            up()
            setpos(x, y)
            left(60)
            down()
            forward(30)


def get_word():
    file = open("dictionnaire.txt", "r")
    lines = file.readlines()

    # Choisir un mot valide dans le dictionnaire
    while True:
        word = random.choice(lines).strip().lower()
        if est_mot_valide(word):
            return word


def play():
    word = get_word()
    tab_lettres_reponse = ["-" for _ in word]
    nb_tries = 0
    nb_tries_max = 7

    while True:
        letter = input("Saisir une lettre sans accent : ")
        if not est_lettre_valide(letter):
            print("Cette letter n'est pas valide")
            continue
        if letter not in word:
            nb_tries += 1
            affiche_element_pendu(nb_tries)
            if nb_tries < nb_tries_max:
                continue
            print(f"Partie perdue, le mot à trouver était : {word}")
            break
        else:
            # on affiche la lettre aux emplacements où elle se trouve dans le mot à chercher
            for i in range(len(word)):
                if word[i] == letter:
                    tab_lettres_reponse[i] = letter
            mot_reponse = "".join(tab_lettres_reponse)
            print(mot_reponse)
            if mot_reponse == word:
                print("Partie gagnée !")
                break

    input()


if __name__ == '__main__':
    play()