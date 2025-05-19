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


# Fonction qui enlève les accents du mot choisi
def enlever_accents(mot) :
    mot_sans_accent = ""
    i = 0
    while i < len(mot) :
        if mot[i] == 'à' or mot[i] == 'â' or mot[i] == 'ä' :
            mot_sans_accent += 'a'
        elif mot[i] == 'é' or mot[i] == 'è' or mot[i] == 'ê' or mot[i] == 'ë' :
            mot_sans_accent += 'e'
        elif mot[i] == 'î' or mot[i] == 'ï' :
            mot_sans_accent += 'i'
        elif mot[i] == 'ô' or mot[i] == 'ö':
            mot_sans_accent += 'o'
        elif mot[i] == 'ù' or mot[i] == 'û' or mot[i] == 'ü' :
            mot_sans_accent += 'u'
        elif mot[i] == 'ç' :
            mot_sans_accent += 'c'
        else :
            mot_sans_accent += mot[i]
        i += 1
    return mot_sans_accent



#Fonction qui demande une lettre à l'utilisateur
def demander_lettre(lettres_deja_donnees):
    lettre = input('Entrez une lettre : ')
    # Boucle pour s'assurer que la lettre n'a pas été donnée avant
    while lettre in lettres_deja_donnees:
        print('Cette lettre a déjà été donnée.')
        lettre = input('Entrez une nouvelle lettre : ')
    lettres_deja_donnees.extend(lettre)
    return lettres_deja_donnees



