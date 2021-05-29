from common_functions import *
from Astar import*

configs = lit('configs')
pathfinding = configs['pathfinding']
distPathfind = 0
print(pathfinding)
if pathfinding:
    distPathfind = 5
else:
    distPathfind = 0

class Joueur:
    def __init__(self, pos):  # initialisation
        self.pos = pos
        self.lastPos = pos
        self.nextPos = pos
        self.score = 0

    def affiche(self, grille):  # affiche le joueur
        grille[self.lastPos[0]][self.lastPos[1]] = '_'
        grille[self.pos[0]][self.pos[1]] = '*'

    def bouge(self, sens, grille):  # bouge le joueur
        self.lastPos = (self.pos[0], self.pos[1])
        if sens == 'G' and self.verifDepl(sens, grille):
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif sens == 'D' and self.verifDepl(sens, grille):
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif sens == 'B' and self.verifDepl(sens, grille):
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif sens == 'H' and self.verifDepl(sens, grille):
            self.pos = (self.pos[0] - 1, self.pos[1])
        self.affiche(grille)

    def verifDepl(self, sens, grille):  # vérifie si le déplacement voulu est valide
        # calcul l'emplacement voulu
        if sens == 'G':
            self.nextPos = (self.pos[0], self.pos[1] - 1)
        elif sens == 'D':
            self.nextPos = (self.pos[0], self.pos[1] + 1)
        elif sens == 'B':
            self.nextPos = (self.pos[0] + 1, self.pos[1])
        else:
            self.nextPos = (self.pos[0] - 1, self.pos[1])

        # et le vérifie
        if not(self.nextPos[0] < 0 or self.nextPos[0] > len(grille)-1 or self.nextPos[1] < 0 or self.nextPos[1] > len(grille)-1):
            if grille[self.nextPos[0]][self.nextPos[1]] == '+':
                return False
            else:
                return True

def verifDeplacement(grille, nextPos):  # vérification de la validité de la prochaine destination
    if not(nextPos[0] < 0 or nextPos[0] > len(grille)-1 or nextPos[1] < 0 or nextPos[1] > len(grille)-1):
        if grille[nextPos[0]][nextPos[1]] == '+' or grille[nextPos[0]][nextPos[1]] == '!' or grille[nextPos[0]][nextPos[1]] == '?':
            return False
        else:
            return True

class Ennemi:
    # TODO Ajouter un moyen de tuer les ennemis
    def __init__(self, pos):  # initialisation
        self.pos = pos
        self.lastPos = pos
        self.nextPos = pos

    def affiche(self, grille):  # Affiche l'ennemi
        grille[self.lastPos[0]][self.lastPos[1]] = '_'
        grille[self.pos[0]][self.pos[1]] = '!'

    def bouge(self, grille, joueur):  # bouge l'ennemi
        self.lastPos = self.pos
        if distanceObj(self, joueur) <= distPathfind:
            pathToPlayer = astar(change2maze(grille), self.pos, joueur.pos)  # Utilise un code venant de https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc
            direction = diffTuple(self.pos, pathToPlayer[1])
            self.nextPos = diffTuple(self.pos, direction)
        else:
            self.nextPos = addTuple(self.pos, (random.randint(-1, 1), random.randint(-1, 1)))
        if verifDeplacement(grille, self.nextPos):
            self.pos = self.nextPos
            self.affiche(grille)

    def updateState(self, grille, joueur):
        if isTouching(self, joueur):
            joueur.score -= 10
            grille[self.pos[0]][self.pos[1]] = '!'
            joueur.pos = (0, 0)
            joueur.lastPos = (joueur.pos[0], joueur.pos[1])
            joueur.affiche(grille)

class Tresor:
    def __init__(self, pos):
        self.pos = pos
        self.state = 1

    def affiche(self, grille):
        grille[self.pos[0]][self.pos[1]] = "?"

    def updateState(self, grille, joueur):
        if isTouching(self, joueur):
            joueur.score += 10
            grille[self.pos[0]][self.pos[1]] = '*'
            self.state = 0
