
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
    piece = Position()

    def __init__(self, x, y):
        self.matrice = [[self.vide for j in range(x)] for i in range(y)]
        
    def affichage(self):
        for ligne in self.matrice:
            print(ligne)

class Piece:
    
    relative_movement = [Position(1,3),Position(3,1),Position(-1,3),Position(3,-1),Position(-1,-3),Position(-3,-1),Position(-3,1),Position(1,-3)]

    def __init__(self):
        pass

    def movement(self, position):
        liste = []
        for i in self.relative_movement:
            liste.append(position + i)
        return liste

    




pl = Plateau(6, 4)
pl.affichage()