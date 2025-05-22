# Pendu

Ce projet consistait à créer un script contenant uniquement des fonctions qui permettrait à l'utilisateur de jouer au pendu. L'utilisateur doit alors deviner un mot en donnant des lettres les unes après les autres qu'il pense être dans ce mot. Il a droit à six erreurs et un indice lui sera offert à sa drenière tentative.

## Fonctions
Le script python contient sept fonctions.
La première fonction s'appelle créer_liste_mots, elle prend un fichier txt en entrée et retourne une liste des mots contenu dans le fichier.
La deuxième fonction s'appelle choisir_mot, elle prend une liste de mots en entrée et renvoie un mot aléatoirement (en utilisant random) de cette liste.
La troisième fonction s'appelle enlever_fonction, elle prend en entrée un mot et renvoie ce mot sans accent.
La quatrième fonction s'appelle demander_lettre, elle prend en entrée une liste de lettre, demande à l'utilisateur une lettre. Si cette lettre est dans la liste, une nouvelle lettre est demandée, sinon elle est ajoutée à la liste et c'est cette lettre qui est renvoyée.
La cinquième fonction s'appelle afficher_mot, elle prend un mot en entrée et une liste de lettres. Si les lettres du mot sont dans la liste, alors elles apparaissent sinon elles sont remplacées par des tirets.
La sixième fonction s'appelle donner_inidce, elle prend en entrée un mot est une liste de lettres qui aurait été déjà données par l'utilisateur. Elle permettrait alors de renvoyé à l'utilisateur une lettre qui n'est pas dans le mot et qui n'a pas encore été testée. 
La dernière fonction s'appelle jouer et permet alors à l'utilisateur de faire une partie de pendu. Elle utilise les fonctions précédentes.

## Comment jouer ? 
L'utilisateur doit tout d'abord télécharger le projet.
Pour lancer une partie, l'utilisateur doit faire tourner le script python nommé lancer_une_partie. Ce script demande à l'utilisateur si il vut jouer avec sa propre liste de mots et permet de jouer en fonction de la réponse. En effet, si il veut jouer avec sa liste de mots, il n'aura qu'à rentrer le nom du fichier txt, fichier qui devra être dans le dossier du jeu si il veut pouvoir l'utiliser. Si il ne veut pas jouer avec une liste particulière, une liste par défaut est fournie.
