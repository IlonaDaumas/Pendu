# Ce script est rempli de fonction permettant à la fin de jouer au jeu du pendu

import random
import os

# Fonction pour créer une liste liste de mots à partir d'un fichier txt
def creer_liste_mots(fichier="mots_pendu.txt"):
    # teste si le fichier existe
    full_filename = os.path.join(fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

    # Transforme la chaine de caracteres en liste
    # le saut de ligne sert de separateur de champs
    word_list = words.split('\n')

    # retourne la liste de mots
    return word_list


# Fonction pour le choix du mot
def choisir_mot(liste_de_mots):
    mot = random.choice(liste_de_mots)
    return


#Fonction qui demande une lettre à l'utilisateur
def demander_lettre(lettres_deja_donnees):
    lettre = input('Entrez une lettre : ')
    # Boucle pour s'assurer que la lettre n'a pas été donnée avant
    while lettre in lettres_deja_donnees:
        print('Cette lettre a déjà été donnée.')
        lettre = input('Entrez une nouvelle lettre : ')
    lettres_deja_donnees.extend(lettre)
    return lettres_deja_donnees


