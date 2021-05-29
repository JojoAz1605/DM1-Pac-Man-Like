# common_functions.py
import pickle
import random
from math import*

# fonctions pickle
def ecriture(obj, fileName):
    file = open(fileName, "wb")  # sauvegarde dans f
    pickle.dump(obj, file)
    file.close()

def lit(fileName):
    file = open(fileName, "rb")
    truc = pickle.load(file)
    file.close()
    return truc

def isTouching(obj1, obj2):
    if obj1.pos == obj2.pos:
        return True
    else:
        return False

def distanceObj(obj1, obj2):
    posObj1 = (obj1.pos[0], obj1.pos[1])
    posObj2 = (obj2.pos[0], obj2.pos[1])
    return sqrt(pow(posObj2[0]-posObj1[0], 2)+pow(posObj2[1]-posObj1[1], 2))  # formule distance entre 2 points

def distance(pos1, pos2):
    return sqrt(pow(pos2[0] - pos1[0], 2) + pow(pos2[1] - pos1[1], 2))  # formule distance entre 2 points

def creegrille(taille, val):
    res = [0] * taille
    for i in range(taille):
        res[i] = [val] * taille
    return res

def change2maze(grille):
    maze = creegrille(len(grille), 0)
    for ligne in range(len(grille)):
        for elem in range(len(grille[ligne])):
            if grille[ligne][elem] == '+' or grille[ligne][elem] == '?':
                maze[ligne][elem] = 1
    return maze

def creeGrille(taille, val):
    res = [0] * taille
    for i in range(taille):
        res[i] = [val] * taille
    return res

def randomPos(min_, max_):
    return random.randint(min_, max_), random.randint(min_, max_)

def diffTuple(tuple1, tuple2):
    return tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]

def addTuple(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]