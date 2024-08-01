import random
import string
from turtle import *


class Hanged:

    def __init__(self):
        self.word = self._get_word()
        self._play()

    def _get_word(self):
        file = open("dictionnaire.txt", "r")
        lines = file.readlines()

        # Choisir un mot valide dans le dictionnaire
        while True:
            word = random.choice(lines).strip().lower()
            if self._is_valid_word(word):
                return word

    def _play(self):
        response_letters = ["-" for _ in self.word]
        nb_errors = 0
        max_nb_errors = 7

        while True:
            letter = input("Saisir une lettre sans accent : ")
            if not self._is_valid_letter(letter):
                print("Lettre non valide")
                continue
            if letter not in self.word:
                nb_errors += 1
                self._show_hanged_element(nb_errors)
                if nb_errors < max_nb_errors:
                    continue
                print(f"\nPartie perdue, le mot à trouver était : {self.word}")
                break
            # on affiche la lettre aux emplacements où elle se trouve dans le mot à chercher
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    response_letters[i] = letter
            response_word = "".join(response_letters)
            print(response_word)
            if response_word == self.word:
                print("\nPartie gagnée !")
                break

        input()

    @staticmethod
    def _is_valid_letter(letter):
        if letter in string.ascii_lowercase:
            return True
        return False

    @staticmethod
    def _is_valid_word(word):
        for letter in word:
            if not Hanged._is_valid_letter(letter):
                return False
        return True

    @staticmethod
    def _show_hanged_element(nb_errors):
        match nb_errors:
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


if __name__ == '__main__':
    Hanged()