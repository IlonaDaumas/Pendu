# Ce script permet à l'utilisateur de lancer une partie de pendu

from Jeu_du_pendu import jouer

print('Bonjour !')
# Demandez à l'utilisateur si il souhaite jouer avec sa propre liste de mots
preference_fichier = input('Si vous souhaitez jouer avec votre liste de mots, entrez oui : ')
# on conditionne selon la réponse
if preference_fichier == 'oui' :
    fichier = input('Entrez le nom de votre fichier : ')
    print(jouer(fichier))
else :
    print(jouer())