Masson Joris

Il faut utiliser le fichier main.py, qui affichera le menu principal, à partir duquel on peut
choisir plusieurs choses:

-Jouer:
    lance le partie jeu, une fois dedans il suffit d'appuyer sur 'jouer' pour lancer le jeu.
        -Contrôles:
            -Les flèches directionnelles du clavier sont utilisées pour se déplacer, mais il
            est aussi possible d'utiliser les boutons prévus pour ça.
        -But:
            -Le but est d'arriver à l'opposé du plateau, en ramassant les trésors en route,
            et en évitant les ennemis.
        -Code couleur:
            -Vert: le joueur
            -Rouge: les ennemis
            -Doré: les trésors
            -Noir: mur
            -Blanc: case vide
            -Violet: case d'arrivée

-Création d'un niveau:
    Permet de créer ses propres grilles.
        -Contrôles:
            -A la souris, il suffit de cliquer sur le type d'objet voulu, puis de cliquer
            quelque part sur la grille pour en placer autant que voulu.
            -Une fois la grille faite, il suffit de lui donner un nom, puis de cliquer
            sur 'sauvegarder'. Il est aussi possible de charger une grille déjà
            existante, en rentrant son nom puis en cliquant sur 'charger'.
        -Note:
            Si le pathfinding est activé, placer plus de 10 ennemis peut être problématique.
-Options:
    Sert à configurer les différentes options du jeu.
        -Contrôles:
            -Il faut sélectionner une option dans le menu, puis changer sa valeur, une fois
            modifiée, il suffit de la sauvegarder avec le bouton juste à côté.
        -Options:
            -Map par défault: pour changer la grille chargée au début d'une partie
            -Génération aléatoire: à activer pour avoir une génération aléatoire d'ennemis et
            de trésors(à utiliser à vos risques et périls). Il faut utiliser les options
            de nombres de trésors et d'ennemis pour configurer combien seront générés
            aléatoirement.
            -Pathfinding: si actif, les ennemis pourront traquer le joueur dans un périmètre
            de 5 cases autour d'eux, en utilisant l'algorithme A*.
                -Note: le programme pour le pathfinding n'est pas de moi, la source est en
                commentaire du programme Astar.py.
                -Note2: si inactif, les ennemis bougeront aléatoirement.
        -Sauvergarde: une fois les options modifiée comme voulues, il faut appuyer sur le bouton
        'sauvegarder et quitter'.
        -Note: il est possible de charger les options par défaut, il suffit de cliquer sur le
        bouton prévu à cet effet.
-Quitter:
    Quitte le jeu.