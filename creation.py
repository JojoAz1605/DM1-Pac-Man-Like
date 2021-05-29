# creation.py
from tkinter import *
from common_functions import *

# variables globales
# valeurs par défaut à lire dans le dictionnaire

configs = lit("configs")
tailleCase = configs["tailleCase"]  # dimension d'une case supposée carrée
x0, y0 = configs["x0"], configs["y0"]  # coordonnées du point en haut à gauche
tailleGrille = configs["tailleGrille"]  # taille de la grille
laGrille = configs["defaultMap"]  # le dessin

crayon = "+"

couleur = {"+": "black", "_": "white", "*": "green", "!": "red", "?": "yellow"}


# black -> mur
# white -> vide
# green -> joueur
# red -> ennemi
# yellow -> tresor

def winCreation():
    global configs, tailleGrille, tailleGrille, x0, y0, laGrille, crayon, couleur

    # fonctions Tkinter
    def retour():  # pour l'instant quitte l'appli et met le dessin en cours dans le dictionnaire puis sauvegarde ce dictionnaire.
        fenCreation.quit()
        fenCreation.destroy()

    def dessineGrille(
            grille):  # dessin de la grille grâce au dico couleur qui fait la correspondance entre le symbole de la grille python et la couleur
        global tailleCase
        leCanvas.delete(ALL)
        n = len(grille)
        for i in range(n + 1):  # dessin des traits de la grille
            leCanvas.create_line(x0 + tailleCase * i, y0, x0 + tailleCase * i, y0 + n * tailleCase)
            leCanvas.create_line(x0, y0 + tailleCase * i, x0 + n * tailleCase, y0 + tailleCase * i)
        for i in range(n):  # coloriage des cases murs non vides
            for j in range(n):
                x = grille[i][j]
                if x != '_':
                    leCanvas.create_rectangle(x0 + tailleCase * j, y0 + tailleCase * i, x0 + tailleCase * (j + 1),
                                              y0 + tailleCase * (i + 1), fill=couleur[x])

    # fonction associée au clic pour dessiner une case

    def murs(
            event):  # gère affichage du clic et mise à jour de la grille grâce au dico couleur qui fait la correspondance entre le symbole de la grille pythpn et la couleur du dessin
        global tailleCase
        [i, j] = correspond(event.x, event.y)
        leCanvas.create_rectangle(x0 + tailleCase * j, y0 + tailleCase * i, x0 + tailleCase * (j + 1),
                                  y0 + tailleCase * (i + 1), fill=couleur[crayon])
        laGrille[i][j] = crayon

    def correspond(x, y):  # transforme la position du clic en case de la grille  attention  à ne pas inverser x et y
        global tailleCase
        return [(y - y0) // tailleCase, (x - x0) // tailleCase]

    # fonctions des boutons
    def sauve():
        global laGrille
        nom = zoneSaisie.get()
        ecriture(laGrille, nom)
        zoneSaisie.delete("0", END)

    def charge():
        global laGrille
        nom = zoneSaisie.get()
        laGrille = lit(nom)
        dessineGrille(laGrille)
        zoneSaisie.delete("0", END)

    def gomme():
        global crayon
        crayon = "_"
        buttonGomme.configure(bg="green")
        buttonMur.configure(bg="light grey")
        buttonEnnemi.configure(bg="light grey")
        buttonTresor.configure(bg="light grey")

    def murNoir():
        global crayon
        crayon = "+"
        buttonGomme.configure(bg="light grey")
        buttonMur.configure(bg="green")
        buttonEnnemi.configure(bg="light grey")
        buttonTresor.configure(bg="light grey")

    def ennemi():
        global crayon
        crayon = "!"
        buttonGomme.configure(bg="light grey")
        buttonMur.configure(bg="light grey")
        buttonEnnemi.configure(bg="green")
        buttonTresor.configure(bg="light grey")

    def tresor():
        global crayon
        crayon = "?"
        buttonGomme.configure(bg="light grey")
        buttonMur.configure(bg="light grey")
        buttonEnnemi.configure(bg="light grey")
        buttonTresor.configure(bg="green")

    def commencer():
        global tailleGrille, laGrille, crayon
        crayon = '+'
        laGrille = creegrille(tailleGrille, '_')
        dessineGrille(laGrille)
        leCanvas.bind("<Button-1>", murs)

    # définitions positionnement des widgets
    fenCreation = Tk()
    fenCreation.title("jeu")

    # canvas
    leCanvas = Canvas(fenCreation, height=600, width=600, bg="white")
    leCanvas.pack(side=LEFT)

    # bouton commencer/recommencer
    buttonNew = Button(fenCreation, text="commencer/recommencer", command=commencer, font=("Ubuntu", 20, "bold"))
    buttonNew.pack(side=TOP, pady=50)

    # cadre pour mettre zone de saisie et laber associé
    cadreSaisie = Frame(fenCreation)
    labelSaisie = Label(cadreSaisie, text=" saisir le nom du fichier :")
    labelSaisie.pack()
    zoneSaisie = Entry(cadreSaisie, width=15)
    zoneSaisie.pack()
    cadreSaisie.pack()

    # bouton de sauvegarde
    buttonSave = Button(cadreSaisie, text="sauvegarde", command=sauve, font=("Ubuntu", 20, "bold"))
    buttonSave.pack(side=TOP)

    # bouton de chargement
    buttonLoad = Button(cadreSaisie, text="charger", command=charge, font=("Ubuntu", 20, "bold"))
    buttonLoad.pack(side=TOP)

    # bouton retour
    buttonQuit = Button(fenCreation, text="retour", command=retour, font=("Ubuntu", 20, "bold"))
    buttonQuit.pack(side=BOTTOM, pady=30)

    # zone de choix gomme/crayon/etc
    CadreCrayon = Frame(fenCreation, bg="cyan")

    buttonGomme = Button(CadreCrayon, text="gomme", command=gomme, font=("Ubuntu", 20, "bold"))
    buttonGomme.pack(side=LEFT)
    buttonMur = Button(CadreCrayon, text="mur", bg="green", command=murNoir, font=("Ubuntu", 20, "bold"))
    buttonMur.pack(side=LEFT)
    buttonEnnemi = Button(CadreCrayon, text="Ennemis", command=ennemi, font=("Ubuntu", 20, "bold"))
    buttonEnnemi.pack(side=LEFT)
    buttonTresor = Button(CadreCrayon, text="Tresors", command=tresor, font=("Ubuntu", 20, "bold"))
    buttonTresor.pack()

    CadreCrayon.pack(side=BOTTOM, pady=20)

    fenCreation.mainloop()
