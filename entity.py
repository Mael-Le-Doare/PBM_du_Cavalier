
class Position:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 

    def __add__(self, other):
        p = Position()
        p.x = other.x + self.x
        p.y = other.y + self.y
        return


class Plateau:
    vide = 0

    def __init__(self, x, y):
        self.matrice = [[self.vide for j in range(x)] for i in range(y)]
        
    def affichage(self):
        for ligne in self.matrice:
            print(ligne)

class Piece:
    
    def __init__(self, x, y, mouvements):
        self.position = Position(x, y)
        

    def movement(self):
        liste = []
        for i in self.relative_movement:
            liste.append(self.position + i)
        return liste
    
    def affichage(self):
        print(self.relative_movement)
        print(self.position)



pl = Plateau(6, 4)
pl.affichage()



def lancement():
    pass

lancement()