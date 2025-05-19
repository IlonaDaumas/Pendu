# Ce script est rempli de fonctions permettant à la fin de jouer au jeu du pendu

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
    #chaîne de caractère étant immuable, il faut créer un nouveau mot sans rien auquel on ajoutera les lettres sans accents du mot
    mot_sans_accent = ""
    i = 0
    # Boucle sur le nombre de lettre du mot
    while i < len(mot) :
        # Conditions pour enlever les accents des lettres avec
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
        # on ajoute 1 à l'indice i pour parcourir la longueur du mot
        i += 1
    return mot_sans_accent



# Fonction qui demande une lettre à l'utilisateur
def demander_lettre(lettres_deja_donnees):
    lettre = input('Entrez une lettre : ')
    # Boucle pour s'assurer que la lettre n'a pas été donnée avant
    while lettre in lettres_deja_donnees:
        print('Cette lettre a déjà été donnée.')
        lettre = input('Entrez une nouvelle lettre : ')
    # on ajoute la nouvelle lettre à la liste des lettres déjà données
    lettres_deja_donnees.extend(lettre)
    return lettres_deja_donnees

# Fonction pour l'affichace caché du mot pendant la partie
def afficher_mot(mot, liste_lettres_trouvees) :
    # on crée un mot vide pour l'instant
    affichage_mot = ""
    i = 0
    while i < len(mot) :
        # si la lettre est trouvée, on l'ajoute à l'affichage
        if mot[i] in liste_lettres_trouvees :
            affichage_mot += mot[i]
        else :
            # si la lettre n'est pas trouvée, on met un tiret
            affichage_mot += '_'
        # on ajoute 1 à l'indice i pour parcourir la longueur du mot
        i += 1
    return affichage_mot


