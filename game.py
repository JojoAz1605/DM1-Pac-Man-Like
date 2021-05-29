# game.py
from tkinter import *
from objets import*

COULEURS = {  # définition des couleurs pour affichage
    "+": "black",  # + -> mur
    "_": "white",  # _ -> vide
    "*": "green",  # * -> joueur
    "!": "red",  # ! -> ennemi
    "?": "gold3",  # ? -> tresor
    "°": "DarkOrchid1"  # ° -> arrivée
}

# valeurs par défaut à lire dans le dictionnaire
configs = lit("configs")

x0, y0 = configs["x0"], configs["y0"]  # coordonnées du point en haut à gauche
tailleGrille = configs["tailleGrille"]  # taille de la grille
tailleCase = configs["tailleCase"]  # dimension d'une case supposée carrée
niveau = lit(configs["defaultMap"])  # le niveau à charger
isRandom = configs["random"]
nbEnnemis = configs["nbFantomes"]
nbTresors = configs["nbTresors"]

nbTresorsPris = 0

listePosEnnemis = []  # la liste des positions d'ennemis
listeEnnemis = []  # la liste des ennemis

listePosTresors = []  # la liste des positions de trésors
listeTresors = []  # la liste des trésors

leJoueur = Joueur((0, 0))  # position du joueur

def winGame():
    global COULEURS, configs, x0, y0, tailleCase, tailleGrille, niveau, isRandom, nbEnnemis, nbTresors, listeTresors, listeEnnemis, listePosTresors, listePosEnnemis
    # fonction de dessin de la grille du fichier des murs
    def dessineGrille(grille):  # dessin de la grille grâce au dico couleur qui fait la correspondance entre le symbole de la grille python et la couleur
        can.delete(ALL)
        n = len(grille)
        for i in range(n + 1):  # dessin des traits de la grille
            can.create_line(x0 + tailleCase * i, y0, x0 + tailleCase * i, y0 + n * tailleCase)
            can.create_line(x0, y0 + tailleCase * i, x0 + n * tailleCase, y0 + tailleCase * i)

        for i in range(n):  # coloriage des cases murs non vides
            for j in range(n):
                x = grille[i][j]
                if x != '_':
                    can.create_rectangle(x0 + tailleCase * j, y0 + tailleCase * i, x0 + tailleCase * (j + 1), y0 + tailleCase * (i + 1), fill=COULEURS[x])

    def clearEnemiesAndTresors():
        global niveau
        for ligne in range(len(niveau)):
            for elem in range(len(niveau)):
                if niveau[ligne][elem] == '!' or niveau[ligne][elem] == '?':
                    niveau[ligne][elem] = '_'

    def getEnnemyPos():  # fait la liste des ennemis de la map
        global listePosEnnemis, niveau, isRandom, nbEnnemis, nbTresors
        posTemp = (0, 0)
        if isRandom:
            clearEnemiesAndTresors()
            for pos in range(nbEnnemis):
                while niveau[posTemp[0]][posTemp[1]] == '+' or niveau[posTemp[0]][posTemp[1]] == '*' or posTemp in listePosEnnemis:
                    posTemp = randomPos(3, len(niveau)-1)
                listePosEnnemis.append(posTemp)
        else:
            for x in range(len(niveau)):
                for y in range(len(niveau[x])):
                    if niveau[x][y] == '!':
                        listePosEnnemis.append((x, y))

    def getTresorPos():  # fait la liste des trésors de la map
        global listePosEnnemis, niveau, isRandom, nbEnnemis, nbTresors
        posTemp = (0, 0)
        if isRandom:
            clearEnemiesAndTresors()
            for pos in range(nbTresors):
                while niveau[posTemp[0]][posTemp[1]] == '+' or niveau[posTemp[0]][posTemp[1]] == '*' or posTemp in listePosTresors:
                    posTemp = randomPos(3, len(niveau) - 1)
                listePosTresors.append(posTemp)
        else:
            for x in range(len(niveau)):
                for y in range(len(niveau[x])):
                    if niveau[x][y] == '?':
                        listePosTresors.append((x, y))

    def deplacement(grille, d):  # deplacement de d à partir de la position pos  version tresor/fantômes/murs
        global niveau, leJoueur, listeEnnemis, listeTresors, nbTresorsPris
        txtMess.configure(text="")
        leJoueur.bouge(d, grille)  # le joueur bouge
        for ennemi in range(len(listeEnnemis)):  # parcours les ennemis
            listeEnnemis[ennemi].bouge(niveau, leJoueur)  # les fait bouger
            listeEnnemis[ennemi].updateState(niveau, leJoueur)
            if distanceObj(leJoueur, listeEnnemis[ennemi]) <= distPathfind:
                txtMess.configure(text="Un ennemi a repéré le joueur!")
        for tresor in range(len(listeTresors)):  # parcours les trésors
            listeTresors[tresor].updateState(niveau, leJoueur)  # vérifie l'état des trésors
            if isTouching(leJoueur, listeTresors[tresor]):
                txtMess.configure(text="Le joueur a trouvé un trésor, il gagne 10 points")
            if listeTresors[tresor].state == 0:  # si le trésor est pris
                listeTresors[tresor].pos = (-1, -1)  # modifie sa position à (-1, -1)
        if distance(leJoueur.pos, (len(niveau)-1, len(niveau)-1)) == 0:
            txtMess.configure(text='Le joueur a gagné avec '+str(leJoueur.score)+" points!")

        labelScore.configure(text="Votre score:" + str(leJoueur.score))  # change l'affichage du score

    #  fonctions Tkinter
    def monquitter():
        fenGame.quit()
        fenGame.destroy()

    # les 4 fonctions de déplacement
    def H(*args):  # haut
        deplacement(niveau, 'H')
        dessineGrille(niveau)

    def D(*args):  # droite
        deplacement(niveau, 'D')
        dessineGrille(niveau)

    def G(*args):  # gauche
        deplacement(niveau, 'G')
        dessineGrille(niveau)

    def B(*args):  # bas
        deplacement(niveau, 'B')
        dessineGrille(niveau)

    def new():  # nouvelle partie
        global configs, niveau, listePosEnnemis, listeEnnemis, listePosTresors, listeTresors, isRandom, nbEnnemis, nbTresors
        niveau = lit(configs['defaultMap'])
        leJoueur.score = 0
        leJoueur.pos = (0, 0)
        niveau[0][0] = '*'
        niveau[len(niveau) - 1][len(niveau) - 1] = '°'
        leJoueur.affiche(niveau)  # Premier affichage du joueur
        listePosEnnemis = []
        listeEnnemis = []
        listePosTresors = []
        listeTresors = []

        getEnnemyPos()
        getTresorPos()
        for pos in listePosEnnemis:
            listeEnnemis.append(Ennemi((pos[0], pos[1])))
        for pos in listePosTresors:
            listeTresors.append(Tresor((pos[0], pos[1])))
        for ennemi in listeEnnemis:
            ennemi.affiche(niveau)  # Premier affichage des ennemis
        for tresor in listeTresors:
            tresor.affiche(niveau)  # Premier affichage des trésors
        dessineGrille(niveau)

    fenGame = Tk()
    fenGame.title("jeu")

    can = Canvas(fenGame, height=600, width=600, bg="white")
    can.pack(side=LEFT)

    bjouer = Button(fenGame, text="jouer", command=new, font=("Ubuntu", 20, "bold"))
    bjouer.pack(side=TOP)

    cadre = Frame(fenGame, pady=20, width=160)
    BH = Button(cadre, command=H, text='H', font=("Ubuntu", 20, "bold"))
    BH.pack()
    cadremilieu = Frame(cadre)
    cadremilieu.pack()
    BG = Button(cadremilieu, command=G, text='G', font=("Ubuntu", 20, "bold"))
    BD = Button(cadremilieu, command=D, text='D', font=("Ubuntu", 20, "bold"))
    BB = Button(cadre, command=B, text='B', font=("Ubuntu", 20, "bold"))
    cadre.pack()

    fenGame.bind('<Right>', D)
    fenGame.bind('<Left>', G)
    fenGame.bind('<Up>', H)
    fenGame.bind('<Down>', B)

    BG.pack(side=LEFT)
    BD.pack(side=LEFT)
    BB.pack()

    bq = Button(fenGame, text="Quitter", command=monquitter, font=("Ubuntu", 20, "bold"))
    bq.pack(side=BOTTOM)

    cadreScore = Frame(fenGame, pady=20, padx=20)
    labelScore = Label(cadreScore, text="Votre score:" + str(leJoueur.score), font=("Ubuntu", 20, "bold"))
    labelScore.pack(side=LEFT)
    cadreScore.pack()

    cadreMessage = Frame(fenGame, pady=50, padx=20)
    cadreMessage.pack(side=BOTTOM)
    labMess = Label(cadreMessage, text="informations:", font=("Ubuntu", 20, "bold"))
    txtMess = Label(cadreMessage, text="", font=("Ubuntu", 18, "bold"))
    labMess.pack(side=TOP)
    txtMess.pack(side=TOP)

    fenGame.mainloop()
