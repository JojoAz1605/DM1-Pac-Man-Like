# options.py
from common_functions import *
from tkinter import*

# Définition des constantes
W_WIDTH = 350  # Largeur de la fenêtre
W_HEIGHT = 200  # Hauteur de la fenêtre
DEFAULT_CONFIG = {  # Configs par défaut
        "tailleGrille": 24,
        "tailleCase": 20,
        "x0": 50,
        "y0": 50,
        "defaultMap": "default",  # La map par défaut
        "random": False,  # Si True, les ennemis et trésors seront générés aléatoirement, en remplaçant ceux présents à la base
        "nbFantomes": 2,  # Le nb d'ennemis générés
        "nbTresors": 3,  # Le nb de tresors générés
        "pathfinding": True  # Détermine si oui ou non, les ennemis pourront suivre le joueur inteligemment
    }
OPTIONS = [
        'Taille de la grille',
        'Taille des cases',
        'x0',
        'y0',
        'Map par défaut',
        'Nombre de fantômes',
        'Nombres de trésors'
    ]
# Définition de variables
configsAct = lit("configs")  # Reprend les configs actuelles
newConfig = configsAct  # Sert de base aux modifications
newConfig['random'] = False  # Sert à éviter un crash du programme(raison inconnue)
newConfig['pathfinding'] = False
print(newConfig)
selec = OPTIONS[0]

def winOptions():
    global W_HEIGHT, W_WIDTH, OPTIONS, DEFAULT_CONFIG, configsAct, newConfig, selec
    # Création et configuration de la fenêtre
    fenOptions = Tk()  # Création de la fenêtre
    fenOptions.geometry(str(W_WIDTH) + 'x' + str(W_HEIGHT))  # Modifie sa taille
    fenOptions.title("Options")  # Modifie son titre

    checkboxValue = BooleanVar(newConfig['random'])  # Valeur de la checkbox pour le random
    checkboxPath = BooleanVar(newConfig['pathfinding'])
    valMenu = StringVar(fenOptions)  # Stock l'option en cours
    valMenu.set(OPTIONS[0])  # Pour éviter que ça apparaisse vide au début

    def updateLabels():  # update les labels selon la valeur de selec
        global selec

        entryAfficheOptions.delete(0, END)
        if selec == OPTIONS[0]:
            labelAfficheOptions.configure(text='Taille de la grille: ')
            entryAfficheOptions.insert(0, newConfig['tailleGrille'])
        elif selec == OPTIONS[1]:
            labelAfficheOptions.configure(text='Taille des cases: ')
            entryAfficheOptions.insert(0, newConfig['tailleCase'])
        elif selec == OPTIONS[2]:
            labelAfficheOptions.configure(text='x0: ')
            entryAfficheOptions.insert(0, newConfig['x0'])
        elif selec == OPTIONS[3]:
            labelAfficheOptions.configure(text='y0: ')
            entryAfficheOptions.insert(0, newConfig['y0'])
        elif selec == OPTIONS[4]:
            labelAfficheOptions.configure(text='Map par défaut: ')
            entryAfficheOptions.insert(0, newConfig['defaultMap'])
        elif selec == OPTIONS[5]:
            labelAfficheOptions.configure(text='Nombre de fantômes: ')
            entryAfficheOptions.insert(0, newConfig['nbFantomes'])
        elif selec == OPTIONS[6]:
            labelAfficheOptions.configure(text='Nombre de trésor: ')
            entryAfficheOptions.insert(0, newConfig['nbTresors'])

    def changeOption(*args):  # Change le label des options
        global newConfig, selec
        selec = valMenu.get()  # Récupère la valeur du menu
        updateLabels()

    def genRandom():
        newConfig['random'] = checkboxValue.get()  # l'assigne au configs

    def pathfind():
        newConfig['pathfinding'] = checkboxValue.get()

    def loadDefault():  # Charge les options par défaut
        global newConfig, DEFAULT_CONFIG
        newConfig = DEFAULT_CONFIG
        updateLabels()

    def saveConfig():  # Sauvegarde les nouvelles configs
        global newConfig, selec

        if selec == OPTIONS[0]:
            newConfig['tailleGrille'] = int(entryAfficheOptions.get())
        elif selec == OPTIONS[1]:
            newConfig['tailleCase'] = int(entryAfficheOptions.get())
        elif selec == OPTIONS[2]:
            newConfig['x0'] = int(entryAfficheOptions.get())
        elif selec == OPTIONS[3]:
            newConfig['y0'] = int(entryAfficheOptions.get())
        elif selec == OPTIONS[4]:
            newConfig['defaultMap'] = entryAfficheOptions.get()
        elif selec == OPTIONS[5]:
            newConfig['nbFantomes'] = int(entryAfficheOptions.get())
        elif selec == OPTIONS[6]:
            newConfig['nbTresors'] = int(entryAfficheOptions.get())

    def quitter():  # Quitte la fenêtre
        ecriture(newConfig, 'configs')
        fenOptions.quit()
        fenOptions.destroy()

    # Interface principale
    frameAfficheOptions = Frame(fenOptions)
    frameAfficheOptions.pack()
    optMenuOptions = OptionMenu(frameAfficheOptions, valMenu, *OPTIONS)
    optMenuOptions.pack()
    labelAfficheOptions = Label(frameAfficheOptions, text='')
    labelAfficheOptions.pack(side=LEFT)
    entryAfficheOptions = Entry(frameAfficheOptions)
    entryAfficheOptions.pack(side=LEFT)
    buttonSave = Button(frameAfficheOptions, text='Sauvegarder', command=saveConfig)
    buttonSave.pack(side=RIGHT)

    changeOption()
    valMenu.trace('w', changeOption)

    # Génération random
    frameRand = Frame(fenOptions)
    frameRand.pack()
    labelRand = Label(frameRand, text='Génération aléatoire des trésors et des fantômes? ')
    labelRand.pack(side=LEFT)
    checkBtnRand = Checkbutton(frameRand, variable=checkboxValue, onvalue=True, offvalue=False, command=genRandom)
    checkBtnRand.pack(side=RIGHT)

    # Pathfinding
    framePath = Frame(fenOptions)
    framePath.pack()
    labelPath = Label(framePath, text='Pathfinding des ennemis? ')
    labelPath.pack(side=LEFT)
    checkBtnPath = Checkbutton(framePath, variable=checkboxPath, onvalue=True, offvalue=False, command=pathfind)
    checkBtnPath.pack(side=LEFT)

    # Boutons divers
    frameConfig = Frame(fenOptions, width=W_WIDTH, height=100)
    frameConfig.pack(side=BOTTOM)
    buttonLoadDefault = Button(frameConfig, text='Charger les options par défaut', command=loadDefault)
    buttonLoadDefault.pack(side=TOP, pady=1)
    buttonQuitter = Button(frameConfig, text='Sauvegarder et quitter', command=quitter)
    buttonQuitter.pack(side=BOTTOM, pady=1)

    fenOptions.mainloop()  # Loop
