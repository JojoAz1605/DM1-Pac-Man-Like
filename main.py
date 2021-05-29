# main.py
from game import*
from creation import*
from options import*

def lanceGame():
    global aLancer
    aLancer = 0
    fenMain.quit()
    fenMain.destroy()

def lanceCreation():
    global aLancer
    aLancer = 1
    fenMain.quit()
    fenMain.destroy()

def lanceOptions():
    global aLancer
    aLancer = 2
    fenMain.quit()
    fenMain.destroy()

def quitter():
    global aLancer
    aLancer = 3
    fenMain.quit()
    fenMain.destroy()


while True:
    aLancer = -1
    fenMain = Tk()

    buttonGame = Button(fenMain, text="Jouer", command=lanceGame)
    buttonGame.pack()
    buttonCreation = Button(fenMain, text="Creation d'un niveau", command=lanceCreation)
    buttonCreation.pack()
    buttonOptions = Button(fenMain, text="Options", command=lanceOptions)
    buttonOptions.pack()
    buttonQuit = Button(fenMain, text="Quitter", command=quitter)
    buttonQuit.pack()

    fenMain.mainloop()
    if aLancer == 0:
        winGame()
    elif aLancer == 1:
        winCreation()
    elif aLancer == 2:
        winOptions()
    elif aLancer == 3:
        break
    else:
        print("Erreur")
