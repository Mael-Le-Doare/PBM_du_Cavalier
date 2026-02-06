
class Position:
    x,y = 0, 0
    
    def __add__(self, other):
        p = Position()
        p.x = other[0] + self.x
        p.y = other[1] + self.y
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
    
    relative_movement = [(1,3),(3,1),(-1,3)(3,-1),(-1,-3),(-3,-1),(-3,1),(1,-3)]

    def __init__(self):
        pass

    def movement(self, position):
        liste = []
        for i in self.relative_movement:
            liste.append(position + i)
        return liste

    




pl = Plateau(6, 4)
pl.affichage()