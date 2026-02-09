import constantes

class Position:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 

    def __add__(self, other):
        p = Position()
        p.x = other.x + self.x
        p.y = other.y + self.y
        return
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)

    def getMat(self,mat):
        return mat[self.x][self.y]

    def setMat(self, mat, val):
        mat[self.x][self.y] = val

class Plateau:
    vide = 0

    def __init__(self, x, y, piece):
        self.matrice = [[self.vide for j in range(x)] for i in range(y)]
        self.piece = piece
        
    def affichage(self):
        for ligne in self.matrice:
            print(ligne)
        self.piece.affichage()

    def bouger(self):
        liste = []
        for move in self.piece:
            if move.x >=0 and move.x <= 7 \
                and move.y >=0 and move.y <= 7 \
                and move.getMat(self.matrice) == 0:
                liste.append(move)
        return liste
            
    def accept(self, x, y):
        pos = Position(x,y)
        if pos in self.bouger():
            self.piece.position()
            return True
        return False

class Piece:
    relative_movements = []

    def __init__(self, x, y, mouvements):
        for pos in mouvements:
            self.relative_movements.append(Position(*pos))
        self.position = Position(x, y)
        

    def movement(self):
        liste = []
        for i in self.relative_movements:
            liste.append(self.position + i)
        return liste
    
    def affichage(self):    
        print(self.relative_movements)
        print(self.position)

def lancement():
    piece = Piece(0,0,constantes.knight)
    pl = Plateau(6, 4, piece)
    pl.affichage()

    return pl

lancement()