# Ce script est rempli de fonctions permettant à la fin à l'utilisateur
# de jouer au jeu du pendu

import random
import os
import string

# Fonction pour créer une liste liste de mots à partir d'un fichier txt
# Cette fonction est pris de Marlène Sanjosé avec quelques changement afin de fonctionner pour le cas
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


# Fonction qui prend une liste de mots et renvoie un des mots aléatoirement
def choisir_mot(liste_de_mots):
    mot = random.choice(liste_de_mots)
    return mot


# Fonction qui enlève les accents du mot donné en entrée
def enlever_accents(mot) :
    # les chaînes de caractères étant immuables, il faut créer un nouveau mot vide
    # auquel on ajoutera les lettres sans accents du mot
    mot_sans_accent = ""
    i = 0
    # Boucle sur le nombre de lettre du mot
    while i < len(mot) :
        # Conditions pour envoyer la lettre sans accent correspondant à la lettre avec accent
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
    # le mot sans accent est renvoyé
    return mot_sans_accent



# Fonction qui demande de rentrer une lettre à l'utilisateur
# cette fonction prend en entrée une liste de lettres déjà données par l'utilisateur
def demander_lettre(lettres_deja_donnees):
    lettre = input('Entrez une lettre : ')
    # Boucle pour s'assurer que la lettre n'a pas été donnée avant
    while lettre in lettres_deja_donnees:
        print('Cette lettre a déjà été donnée.')
        lettre = input('Entrez une nouvelle lettre : ')
    # on ajoute la nouvelle lettre à la liste des lettres déjà données
    lettres_deja_donnees.extend(lettre)
    # la lettre donnée par l'utilisateur est renvoyée
    return lettre

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
    # on renvoie le mot avec les ettres trouvées et les tirets
    return affichage_mot

# Fonction pour donner un indice, soit une lettre qui ne fait pas partie de mot
# et qui n'a pas été donnée
def donner_indice(mot,  liste_lettres_donnees) :
    # on définit une chaine de caractère avec toutes les lettres de l'alphabet
    alphabet = string.ascii_lowercase
    # on met les lettres de l'alphabet dans une liste
    liste_alphabet = list(alphabet)
    # on met les lettres du mot dans une liste
    liste_lettres_mots = list(mot)
    # on crée une liste vide qui contiendra les lettres du mot qui n'ont pas encore
    # été donné par l'utilisateur
    liste_lettres_non_presentes = []
    # on crée une boucle sur toutes les lettres de la liste alphabet
    for lettre in liste_alphabet :
        # on fait une condition de façon à ce que si la lettre de l'alphabet n'est ni dans le mot
        # ni dans la liste des lettres données, elle est mise dans la liste vide
        # créée précédemment
        if (lettre not in liste_lettres_mots) and (lettre not in liste_lettres_donnees) :
            liste_lettres_non_presentes += lettre
        else :
            liste_lettres_non_presentes = liste_lettres_non_presentes
    # avec random on choisit une des lettres du mot qui n'a pas été donnée
    lettre_indice = random.choice(liste_lettres_non_presentes)
    # on renvoie cette lettre
    return lettre_indice



# Fonction qui permet de faire une partie de pendu
def jouer(fichier="mots_pendu.txt") :
    print('Bonjour et bienvenue dans cette nouvelle partie du jeu du pendu')
    # on crée la liste des mots  possibles
    liste_mots_possibles = creer_liste_mots(fichier)
    # le mot est choisi aléatoirement
    mot = choisir_mot(liste_mots_possibles)
    # on enlève les accents au mot
    mot_sans_accent = enlever_accents(mot)
    # on crée une liste vide à laquelle on ajoutera les lettres testées au cours de la partie
    liste_lettres_testées = []
    # on affiche le mot sans les lettres pour que l'utilisateur puisse connaitre le nombre de lettres
    mot_affichage = afficher_mot(mot_sans_accent, liste_lettres_testées)
    print(mot_affichage)
    # on initialise le nombre de tentatives à 0
    tentatives = 0

    # on boucle tant que le mot n'est pas trouvé et tant que le nombre d'erreur est inférieure à 6
    while ('_' in mot_affichage) and tentatives < 6 :
        # on demande une lettre l'utilisateur
        lettre_testee = demander_lettre(liste_lettres_testées)
        # on affiche le mot en prenant en compte cette nouvelle lettre
        mot_affichage = afficher_mot(mot_sans_accent, liste_lettres_testées)
        print(mot_affichage)

        # on ajoute 1 aux nombres de tentatives si la lettre n'est pas dans le mot
        if lettre_testee not in mot_sans_accent:
            tentatives += 1
            print("Cette lettre ne fait pas partie du mot.")
            # on ajoute la fonction indice qui donnera une lettre non présente dans le mot avant
            # la dernière tentative de l'utilisateur
            if tentatives == 5:
                indice = donner_indice(mot_sans_accent, liste_lettres_testées)
                print('La lettre ', indice, ' ne fait pas partie du mot que vous recherchez')

        else:
            print("Cette lettre fait partie du mot !")

    # après les 6 tentatives, si il reste des tirets dans le mot caché, la partie est perdue
    if '_' in mot_affichage :
        print('Désolé vous avez perdu la partie, le mot était : ', mot)
    # sinon la partie est gagnée
    else :
        print('Bravo vous avez gagné, le mot était bien : ', mot)

    # demander à l'utilisateur si il veur rejouer
    nouvelle_partie = input('Entrez oui si vous voulez rejouer, non sinon : ')
    if nouvelle_partie == 'oui' :
        print(jouer(fichier))
    else :
        print('Bonne journée !')
    return

