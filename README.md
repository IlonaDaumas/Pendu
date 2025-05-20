# Pendu
Le script python contient six fonctions.
La première fonction s'appelle créer_liste_mots, elle prend un fichier txt en entrée et retourne une liste des mots contenu dans le fichier.
La deuxième fonction s'appelle choisir_mot, elle prend une liste de mots en entrée et renvoie un mot aléatoirement (en utilisant random) de cette liste.
La troisième fonction s'appelle enlever_fonction, elle prend en entrée un mot et renvoie ce mot sans accent.
La quatrième fonction s'appelle demander_lettre, elle prend en entrée une liste de lettre, demande à l'utilisateur une lettre. Si cette lettre est dans la liste, une nouvelle lettre est demandée, sinon elle est ajoutée à la liste et c'est cette lettre qui est renvoyée.
La cinquième fonction s'appelle afficher_mot, elle prend un mot en entrée et une liste de lettre. Si les lettres du mot sont dans la liste, alors elles apparaissent sinon elles sont remplacées par des tirets.
La dernière fonction s'appelle jouer et prend en entrée un fichier txt. Elle permet de créer une liste de mot avec la fonction créer_liste_mots, de récupérer un mot avec la fonction choisir_mot et d'en enlever les accents avec enlever_accents. Ensuite une liste vide est initialisée ainsi qu'une variable tentative. Le mot est alors entièrement affiché avec des tirets à l'aide de la fonction afficher_mot. Une boucle est alors réalisé tant que le mot n'est pas trouvé et que l'utilisateur n'a pas fait plus de 6 erreurs.
